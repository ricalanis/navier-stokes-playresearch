#!/usr/bin/env python3
"""
Run the Navier-Stokes Proof Search Engine.

This script performs a systematic symbolic exploration of the proof space
for the NS regularity problem, searching for paths from known lemmas
to the target: ||u||_{L^2(B(r))} <= C r^beta with beta > 0.05

Usage:
    python scripts/run_proof_search.py [options]

Options:
    --max-depth N       Maximum search depth (default: 10)
    --beam-width N      Beam search width (default: 100)
    --max-nodes N       Maximum nodes to explore (default: 10000)
    --export FILE       Export knowledge base to JSON file
    --quiet             Suppress detailed output
    --gap-only          Only run gap analysis, skip search
"""

import argparse
import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.discovery.proof_search import (
    KnowledgeBase,
    ProofSearchEngine,
    ProofVisualizer,
    GapDetector,
    run_proof_search,
    run_gap_analysis,
    export_knowledge_base,
)


def main():
    parser = argparse.ArgumentParser(
        description="NS Proof Search Engine",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Standard search
  python scripts/run_proof_search.py

  # Deep search with more nodes
  python scripts/run_proof_search.py --max-depth 15 --max-nodes 50000

  # Export knowledge base
  python scripts/run_proof_search.py --export ns_kb.json

  # Gap analysis only
  python scripts/run_proof_search.py --gap-only
"""
    )

    parser.add_argument("--max-depth", type=int, default=10,
                        help="Maximum search depth")
    parser.add_argument("--beam-width", type=int, default=100,
                        help="Beam search width (top-k candidates)")
    parser.add_argument("--max-nodes", type=int, default=10000,
                        help="Maximum nodes to explore")
    parser.add_argument("--export", type=str, default=None,
                        help="Export knowledge base to JSON file")
    parser.add_argument("--quiet", action="store_true",
                        help="Suppress detailed output")
    parser.add_argument("--gap-only", action="store_true",
                        help="Only run gap analysis")

    args = parser.parse_args()

    print("=" * 70)
    print("NAVIER-STOKES PROOF SEARCH ENGINE")
    print("Target: ||u||_{L^2(B(r))} <= C r^beta with beta > 0.05")
    print("=" * 70)
    print()

    # Initialize knowledge base
    kb = KnowledgeBase()

    if not args.quiet:
        print(kb.summary())
        print()

    # Export if requested
    if args.export:
        export_knowledge_base(args.export)
        print(f"\nKnowledge base exported to: {args.export}")

    # Run gap analysis if requested
    if args.gap_only:
        print("\n" + "=" * 70)
        print("RUNNING GAP ANALYSIS ONLY")
        print("=" * 70 + "\n")
        run_gap_analysis(verbose=True)
        return

    # Run proof search
    print("\n" + "=" * 70)
    print("STARTING PROOF SEARCH")
    print("=" * 70)
    print(f"Configuration:")
    print(f"  Max depth: {args.max_depth}")
    print(f"  Beam width: {args.beam_width}")
    print(f"  Max nodes: {args.max_nodes}")
    print()

    engine = ProofSearchEngine(kb)
    result = engine.search(
        target_id="TARGET_LOCAL_DECAY",
        max_depth=args.max_depth,
        beam_width=args.beam_width,
        max_nodes=args.max_nodes
    )

    # Display results
    print(ProofVisualizer.format_search_result(result))

    # Always run gap analysis
    print("\n")
    run_gap_analysis(verbose=True)

    # Summary
    print("\n" + "=" * 70)
    print("FINAL SUMMARY")
    print("=" * 70)
    print(f"Proof found: {result.success}")
    print(f"Nodes explored: {result.explored_nodes}")
    print(f"Max depth reached: {result.max_depth_reached}")
    print(f"Missing lemmas identified: {len(result.missing_lemmas)}")

    if result.missing_lemmas:
        print("\nKey missing lemmas:")
        for i, lemma in enumerate(result.missing_lemmas[:3], 1):
            print(f"  {i}. {lemma}")

    print("\n" + "=" * 70)
    print("INTERPRETATION")
    print("=" * 70)
    if not result.success:
        print("""
The proof search did NOT find a complete proof path from known results
to the target ||u||_{L^2(B(r))} <= C r^beta.

This is EXPECTED - the Millennium Prize problem remains open because
no such proof path exists with current mathematical tools.

The GAP ANALYSIS above identifies exactly what is missing:
1. Local L^2 decay from Type II structure
2. Concentration exclusion (cascade prevention)
3. L^3 boundedness from energy bounds

These gaps are FUNDAMENTAL - they represent the true mathematical
frontier of the NS regularity problem.
""")
    else:
        print("UNEXPECTED: A proof path was found!")
        print("This requires careful verification as it would be a breakthrough.")


if __name__ == "__main__":
    main()
