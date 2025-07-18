class MemoryBlock:
    """Represents a block of memory."""
    def __init__(self, size):
        self.size = size
        self.is_free = True  # Initially, all blocks are free

class MemoryManager:
    """Manages memory allocation and deallocation."""
    def __init__(self, total_size):
        self.memory = [MemoryBlock(total_size)]  # One large free block initially

    def first_fit(self, size):
        """Allocate memory using the First-Fit algorithm."""
        for block in self.memory:
            if block.is_free and block.size >= size:
                self._allocate_block(block, size)
                print(f"Allocated {size} units using First-Fit.")
                return
        print(f"Failed to allocate {size} units using First-Fit.")

    def best_fit(self, size):
        """Allocate memory using the Best-Fit algorithm."""
        best_block = None
        for block in self.memory:
            if block.is_free and block.size >= size:
                if best_block is None or block.size < best_block.size:
                    best_block = block
        if best_block:
            self._allocate_block(best_block, size)
            print(f"Allocated {size} units using Best-Fit.")
        else:
            print(f"Failed to allocate {size} units using Best-Fit.")

    def worst_fit(self, size):
        """Allocate memory using the Worst-Fit algorithm."""
        worst_block = None
        for block in self.memory:
            if block.is_free and block.size >= size:
                if worst_block is None or block.size > worst_block.size:
                    worst_block = block
        if worst_block:
            self._allocate_block(worst_block, size)
            print(f"Allocated {size} units using Worst-Fit.")
        else:
            print(f"Failed to allocate {size} units using Worst-Fit.")

    def free_memory(self, block_index):
        """Free the allocated memory block."""
        if 0 <= block_index < len(self.memory):
            block = self.memory[block_index]
            block.is_free = True
            print(f"Freed {block.size} units of memory at block {block_index}.")
            self._merge_free_blocks()
        else:
            print(f"Invalid block index {block_index}.")

    def _allocate_block(self, block, size):
        """Helper function to allocate memory within a block."""
        if block.size > size:
            new_block = MemoryBlock(block.size - size)
            self.memory.insert(self.memory.index(block) + 1, new_block)
        block.size = size
        block.is_free = False

    def _merge_free_blocks(self):
        """Merge adjacent free blocks into a single block."""
        i = 0
        while i < len(self.memory) - 1:
            if self.memory[i].is_free and self.memory[i + 1].is_free:
                self.memory[i].size += self.memory[i + 1].size
                del self.memory[i + 1]
            else:
                i += 1

    def display_memory(self):
        """Display the current state of memory."""
        print("Memory Blocks:")
        for i, block in enumerate(self.memory):
            status = "Free" if block.is_free else "Allocated"
            print(f"Block {i}: {block.size} units ({status})")
        print("-" * 30)


# Example usage:
if __name__ == "__main__":
    manager = MemoryManager(total_size=100)  # Initialize memory with 100 units

    # Perform some allocations
    manager.first_fit(20)
    manager.best_fit(15)
    manager.worst_fit(30)

    # Display the current state of memory
    manager.display_memory()

    # Free a block of memory
    manager.free_memory(1)  # Free the second block

    # Display the memory state after deallocation
    manager.display_memory()
