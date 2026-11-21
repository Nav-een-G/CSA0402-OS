# ASS4 CO4 – Operating Systems

Student: Naveen G | Register No.: 192411019

## Project Description
This repository contains C programs developed as part of the Operating Systems Assignment (ASS4 CO4).

The programs demonstrate file allocation and disk scheduling algorithms.

## Programs Included

### 1. Contiguous File Allocation
- Demonstrates contiguous memory block allocation for files.
- Displays the starting block and allocated blocks of each file.
- Programming Language: C

### 2. FCFS Disk Scheduling
- Implements First Come First Serve disk scheduling.
- Processes disk requests in arrival order.
- Calculates total head movement.
- Programming Language: C

### 3. SSTF Disk Scheduling
- Implements Shortest Seek Time First.
- Selects the nearest disk request.
- Calculates total head movement.
- Programming Language: C

## Technologies Used
- Programming Language: C
- Compiler: GCC
- Platform: Windows / Linux
- Version Control: Git and GitHub

## How to Run

Step 1: Download or clone this repository.

Step 2: Open the terminal in the project folder.

Step 3: Compile the program.

For Contiguous Allocation:

```bash
gcc contiguous_allocation.c -o allocation
```

For FCFS:

```bash
gcc fcfs_disk_scheduling.c -o fcfs
```

For SSTF:

```bash
gcc sstf_disk_scheduling.c -o sstf
```

Step 4: Execute the program.

```bash
./allocation
./fcfs
./sstf
```

On Windows, run the generated `.exe` files.

## Learning Outcomes
- Understanding file allocation methods.
- Learning disk scheduling algorithms.
- Calculating disk head movement.
- Implementing Operating System concepts using C.

## Author
Operating Systems Student

## Conclusion
This repository demonstrates basic Operating Systems concepts through simple C programs. It helps understand file allocation and disk scheduling techniques through practical implementation.