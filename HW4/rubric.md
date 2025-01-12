
## Rough Rubric

* BitSeq: 20pts (5pts via inspection)
  * getBitsAsString-- 5
  * packBits-- 5
  * getBit-- 5
* FreqTable: 15pts  (5 pts: inspection)
  * clear-- 1
  * populate-- 5
  * getCharCount-- 3
  * printTable-- 1
* HTree: 45pts  (5 pts: inspection)
  * getCharCount-- 10
  * getCharPath-- 10
  * serialize-- 10
  * deserialize-- 10
* createHuffmanTree: 35pts
  * 30 pts "it works"; 5 pts inspection
* LookupTable: 25pt (5 pts inspection)
  * setEncoding-- 5
  * getEncoding-- 5
  * populateFromHuffmanTree-- 10
* Encoder: 30pts  (5 pts inspection)
  * encode-- 25pts
* Decoder: 30pts (5 pts inspection)
  * traverse the tree to recover the chars
  * decode-- 25pts

200 pts 

## Notes

* For each of the chunks identified above, "By Inspection" means that the grader will review the implementation. They are looking for: 
  * Is it "reasonably" efficient-- are you re-using existing functionality, or copying/pasting? 
  * Is it "reasonably" readable-- can we figure out what the code is supposed to be doing by reading it? 
  * Does it look like a human wrote it? 
  * Are you trying to use concepts we've covered in class so far, like a queue/stack/heap/etc? 
