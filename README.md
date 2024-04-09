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

 

 
  
