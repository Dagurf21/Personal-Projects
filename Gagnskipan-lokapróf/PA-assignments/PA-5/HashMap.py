from bucket import *

class HashMap:
    # Create empty bucket list of give size
    def __init__(self, size) -> None:
        self.bucket_count = 4
        self._init_bucket_list()

    def _init_bucket_list(self):
        self.bucket_list = [Bucket() for _ in range(self.size)]
        self.size = 0

    def _check_size_and_rebuild(self):
        if self.size > (self.bucket_count * 1.2):
            old_bucket_list = self.bucket_list
            self.bucket_count = 2 * self.bucket_count
            self._init_bucket_list()
            for bucket in old_bucket_list:
                while len(bucket) > 0:
                    key, data = bucket.pop_next()
                    self.insert(key, data)


    def insert(self, key, data):
        self._check_size_and_rebuild()
        bucket_index = hash(key) % self.bucket_count
        self.bucket_list[bucket_index].insert(key, data)
        self.size += 1

    def update(self, key, data):
        bucket_index = hash(key) % self.bucket_count
        self.bucket_list[bucket_index].update(key, data)

    def find(self, key):
        bucket_index = hash(key) % self.bucket_count
        return self.bucket_list[bucket_index].find(key)

  


    def __str__(self):
        return "".join(str(item) for item in self.hash_table)
    

hash_table = HashTable(50)
 
# insert some values
hash_table.insert('gfg@example.com', 'some value')
print(hash_table)
print()
 
hash_table.insert('portal@example.com', 'some other value')
print(hash_table)
print()
 
# search/access a record with key

# Update
hash_table.remove('portal@example.com')
