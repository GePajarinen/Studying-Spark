BigDataUniversity BD0211EN
Spark Fundamentals I (IBM)
As part of the course Big Data Foundations (https://cognitiveclass.ai/learn/big-data/)

- Resilient Distributet Dataset (RDD)
- Fault-tolerant collection of elemnts that can be operated in parallel.
- Immutable
3 methods for creating RDD:
  1. Parallelizing an existing collection
  2. Referencing a dataset
  3. Transformation from an existing RDD

  2 types of operations:
  1. Transformations
  2. Actions

 I should check some of the transformations in the docuemntation.
 And some of the actions, as well.

RDD persistence:
Each node stores any partition of the cache that it computes in memory.
Reuses them in other actions on that dataset (or dataset derived from it).
   (Future actions are much faster)
2 methods for RDD persistence:
1. persist()
2. cache() -> just persist with the MEMORY_ONLY storage.

<img width="432" alt="image" src="https://github.com/GePajarinen/Studying-Spark/assets/58811514/66ea458f-c25a-4e50-90e6-85d70c01ee44">

## Which storage level to choose?
If your RDDs fit with the default storage level (MEMORY_ONLY), just leave it as it is. This is the most CPU_efficent option.

If not, try to use MEMORY_ONLY_SER and selecting a fast serialization library to make the objects much more space-efficient, but still reasonably fast.

Do not spill to disk unless the functions that compute your dataset are filtering a large amount of data. Otherwise, recomputing a partition may be fast as reading it from disk.

Use the replicated storage levels if you want fast fault recovery (e.g. if using Spark to serve requests from a web app). All the storage levels provide full fault tolerance by recomputing lost data, but the replicated ones let you continue running tasks on the RDD without waiting to recompute a lost partition. 

In env. with high amounts of memory or ultiple apps, the experimental OFF_HEAP mode has several advantages:
- It allows multiple executors to share the same pool of memory in Tachyon.
- It significantly reduce garbage collection costs.
- Cached data is not lost if individual executors crash.

  

 ** ADD the venv conf.
  
