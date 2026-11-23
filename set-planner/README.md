# Set planner
Plan a festival afternoon when stages overlap. Assign points to each band, then find the highest-scoring sequence of complete sets you can attend. Sets may meet at an endpoint. Walking time is assumed to be zero.

With JDK 17+ run `java Planner.java festival.tsv` from this folder. Expect Juniper, Soft Signal and Last Train for **14 points**. Choosing the highest-rated band first would earn only 12.

The planner sorts by end time, finds the last compatible prefix by binary search, and reconstructs the winning sequence from its dynamic programming table. Runtime is O(n log n). The input uses four tab-separated fields per row, with times in minutes from festival opening.

**Make it yours.** Add five minutes between sets and explain how the sample itinerary changes.
