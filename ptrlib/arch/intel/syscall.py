# This package is not directly exposed
import functools

try:
    cache = functools.cache
except AttributeError:
    cache = functools.lru_cache


class SyscallTableIntel(object):
    def __init__(self, bits: int):
        self.bits = bits

    @cache
    def __getitem__(self, name: str):
        if self.bits == 32:
            if name in _syscall_table_32:
                return _syscall_table_32[name]

        else:
            if name in _syscall_table_64:
                return _syscall_table_64[name]

        raise KeyError("No such system call: {}".format(name))

    def __getattr__(self, name: str):
        return self[name]

_syscall_table_32 = {'restart_syscall': 0, 'exit': 1, 'fork': 2, 'read': 3, 'write': 4, 'open': 5, 'close': 6, 'waitpid': 7, 'creat': 8, 'link': 9, 'unlink': 10, 'execve': 11, 'chdir': 12, 'time32': 13, 'mknod': 14, 'chmod': 15, 'lchown16': 16, 'stat': 18, 'lseek': 19, 'getpid': 20, 'mount': 21, 'oldumount': 22, 'setuid16': 23, 'getuid16': 24, 'stime32': 25, 'ptrace': 26, 'alarm': 27, 'fstat': 28, 'pause': 29, 'utime32': 30, 'access': 33, 'nice': 34, 'sync': 36, 'kill': 37, 'rename': 38, 'mkdir': 39, 'rmdir': 40, 'dup': 41, 'pipe': 42, 'times': 43, 'brk': 45, 'setgid16': 46, 'getgid16': 47, 'signal': 48, 'geteuid16': 49, 'getegid16': 50, 'acct': 51, 'umount': 52, 'ioctl': 54, 'fcntl': 55, 'setpgid': 57, 'olduname': 59, 'umask': 60, 'chroot': 61, 'ustat': 62, 'dup2': 63, 'getppid': 64, 'getpgrp': 65, 'setsid': 66, 'sigaction': 67, 'sgetmask': 68, 'ssetmask': 69, 'setreuid16': 70, 'setregid16': 71, 'sigsuspend': 72, 'sigpending': 73, 'sethostname': 74, 'setrlimit': 75, 'old_getrlimit': 76, 'getrusage': 77, 'gettimeofday': 78, 'settimeofday': 79, 'getgroups16': 80, 'setgroups16': 81, 'old_select': 82, 'symlink': 83, 'lstat': 84, 'readlink': 85, 'uselib': 86, 'swapon': 87, 'reboot': 88, 'old_readdir': 89, 'old_mmap': 90, 'munmap': 91, 'truncate': 92, 'ftruncate': 93, 'fchmod': 94, 'fchown16': 95, 'getpriority': 96, 'setpriority': 97, 'statfs': 99, 'fstatfs': 100, 'ioperm': 101, 'socketcall': 102, 'syslog': 103, 'setitimer': 104, 'getitimer': 105, 'newstat': 106, 'newlstat': 107, 'newfstat': 108, 'uname': 109, 'iopl': 110, 'vhangup': 111, 'ni_syscall': 166, 'wait4': 114, 'swapoff': 115, 'sysinfo': 116, 'ipc': 117, 'fsync': 118, 'sigreturn': 119, 'clone': 120, 'setdomainname': 121, 'newuname': 122, 'modify_ldt': 123, 'adjtimex_time32': 124, 'mprotect': 125, 'sigprocmask': 126, 'init_module': 128, 'delete_module': 129, 'quotactl': 131, 'getpgid': 132, 'fchdir': 133, 'sysfs': 135, 'personality': 136, 'setfsuid16': 138, 'setfsgid16': 139, 'llseek': 140, 'getdents': 141, 'select': 142, 'flock': 143, 'msync': 144, 'readv': 145, 'writev': 146, 'getsid': 147, 'fdatasync': 148, 'mlock': 150, 'munlock': 151, 'mlockall': 152, 'munlockall': 153, 'sched_setparam': 154, 'sched_getparam': 155, 'sched_setscheduler': 156, 'sched_getscheduler': 157, 'sched_yield': 158, 'sched_get_priority_max': 159, 'sched_get_priority_min': 160, 'sched_rr_get_interval_time32': 161, 'nanosleep_time32': 162, 'mremap': 163, 'setresuid16': 164, 'getresuid16': 165, 'poll': 168, 'setresgid16': 170, 'getresgid16': 171, 'prctl': 172, 'rt_sigreturn': 173, 'rt_sigaction': 174, 'rt_sigprocmask': 175, 'rt_sigpending': 176, 'rt_sigtimedwait_time32': 177, 'rt_sigqueueinfo': 178, 'rt_sigsuspend': 179, 'ia32_pread64': 180, 'ia32_pwrite64': 181, 'chown16': 182, 'getcwd': 183, 'capget': 184, 'capset': 185, 'sigaltstack': 186, 'sendfile': 187, 'vfork': 190, 'getrlimit': 191, 'mmap_pgoff': 192, 'ia32_truncate64': 193, 'ia32_ftruncate64': 194, 'stat64': 195, 'lstat64': 196, 'fstat64': 197, 'lchown': 198, 'getuid': 199, 'getgid': 200, 'geteuid': 201, 'getegid': 202, 'setreuid': 203, 'setregid': 204, 'getgroups': 205, 'setgroups': 206, 'fchown': 207, 'setresuid': 208, 'getresuid': 209, 'setresgid': 210, 'getresgid': 211, 'chown': 212, 'setuid': 213, 'setgid': 214, 'setfsuid': 215, 'setfsgid': 216, 'pivot_root': 217, 'mincore': 218, 'madvise': 219, 'getdents64': 220, 'fcntl64': 221, 'gettid': 224, 'ia32_readahead': 225, 'setxattr': 226, 'lsetxattr': 227, 'fsetxattr': 228, 'getxattr': 229, 'lgetxattr': 230, 'fgetxattr': 231, 'listxattr': 232, 'llistxattr': 233, 'flistxattr': 234, 'removexattr': 235, 'lremovexattr': 236, 'fremovexattr': 237, 'tkill': 238, 'sendfile64': 239, 'futex_time32': 240, 'sched_setaffinity': 241, 'sched_getaffinity': 242, 'set_thread_area': 243, 'get_thread_area': 244, 'io_setup': 245, 'io_destroy': 246, 'io_getevents_time32': 247, 'io_submit': 248, 'io_cancel': 249, 'ia32_fadvise64': 250, 'exit_group': 252, 'epoll_create': 254, 'epoll_ctl': 255, 'epoll_wait': 256, 'remap_file_pages': 257, 'set_tid_address': 258, 'timer_create': 259, 'timer_settime32': 260, 'timer_gettime32': 261, 'timer_getoverrun': 262, 'timer_delete': 263, 'clock_settime32': 264, 'clock_gettime32': 265, 'clock_getres_time32': 266, 'clock_nanosleep_time32': 267, 'statfs64': 268, 'fstatfs64': 269, 'tgkill': 270, 'utimes_time32': 271, 'ia32_fadvise64_64': 272, 'mbind': 274, 'get_mempolicy': 275, 'set_mempolicy': 276, 'mq_open': 277, 'mq_unlink': 278, 'mq_timedsend_time32': 279, 'mq_timedreceive_time32': 280, 'mq_notify': 281, 'mq_getsetattr': 282, 'kexec_load': 283, 'waitid': 284, 'add_key': 286, 'request_key': 287, 'keyctl': 288, 'ioprio_set': 289, 'ioprio_get': 290, 'inotify_init': 291, 'inotify_add_watch': 292, 'inotify_rm_watch': 293, 'migrate_pages': 294, 'openat': 295, 'mkdirat': 296, 'mknodat': 297, 'fchownat': 298, 'futimesat_time32': 299, 'fstatat64': 300, 'unlinkat': 301, 'renameat': 302, 'linkat': 303, 'symlinkat': 304, 'readlinkat': 305, 'fchmodat': 306, 'faccessat': 307, 'pselect6_time32': 308, 'ppoll_time32': 309, 'unshare': 310, 'set_robust_list': 311, 'get_robust_list': 312, 'splice': 313, 'ia32_sync_file_range': 314, 'tee': 315, 'vmsplice': 316, 'move_pages': 317, 'getcpu': 318, 'epoll_pwait': 319, 'utimensat_time32': 320, 'signalfd': 321, 'timerfd_create': 322, 'eventfd': 323, 'ia32_fallocate': 324, 'timerfd_settime32': 325, 'timerfd_gettime32': 326, 'signalfd4': 327, 'eventfd2': 328, 'epoll_create1': 329, 'dup3': 330, 'pipe2': 331, 'inotify_init1': 332, 'preadv': 333, 'pwritev': 334, 'rt_tgsigqueueinfo': 335, 'perf_event_open': 336, 'recvmmsg_time32': 337, 'fanotify_init': 338, 'fanotify_mark': 339, 'prlimit64': 340, 'name_to_handle_at': 341, 'open_by_handle_at': 342, 'clock_adjtime32': 343, 'syncfs': 344, 'sendmmsg': 345, 'setns': 346, 'process_vm_readv': 347, 'process_vm_writev': 348, 'kcmp': 349, 'finit_module': 350, 'sched_setattr': 351, 'sched_getattr': 352, 'renameat2': 353, 'seccomp': 354, 'getrandom': 355, 'memfd_create': 356, 'bpf': 357, 'execveat': 358, 'socket': 359, 'socketpair': 360, 'bind': 361, 'connect': 362, 'listen': 363, 'accept4': 364, 'getsockopt': 365, 'setsockopt': 366, 'getsockname': 367, 'getpeername': 368, 'sendto': 369, 'sendmsg': 370, 'recvfrom': 371, 'recvmsg': 372, 'shutdown': 373, 'userfaultfd': 374, 'membarrier': 375, 'mlock2': 376, 'copy_file_range': 377, 'preadv2': 378, 'pwritev2': 379, 'pkey_mprotect': 380, 'pkey_alloc': 381, 'pkey_free': 382, 'statx': 383, 'arch_prctl': 384, 'io_pgetevents_time32': 385, 'rseq': 386, 'semget': 393, 'semctl': 394, 'shmget': 395, 'shmctl': 396, 'shmat': 397, 'shmdt': 398, 'msgget': 399, 'msgsnd': 400, 'msgrcv': 401, 'msgctl': 402, 'clock_gettime': 403, 'clock_settime': 404, 'clock_adjtime': 405, 'clock_getres': 406, 'clock_nanosleep': 407, 'timer_gettime': 408, 'timer_settime': 409, 'timerfd_gettime': 410, 'timerfd_settime': 411, 'utimensat': 412, 'pselect6': 413, 'ppoll': 414, 'io_pgetevents': 416, 'recvmmsg': 417, 'mq_timedsend': 418, 'mq_timedreceive': 419, 'semtimedop': 420, 'rt_sigtimedwait': 421, 'futex': 422, 'sched_rr_get_interval': 423, 'pidfd_send_signal': 424, 'io_uring_setup': 425, 'io_uring_enter': 426, 'io_uring_register': 427, 'open_tree': 428, 'move_mount': 429, 'fsopen': 430, 'fsconfig': 431, 'fsmount': 432, 'fspick': 433, 'pidfd_open': 434, 'clone3': 435, 'close_range': 436, 'openat2': 437, 'pidfd_getfd': 438, 'faccessat2': 439, 'process_madvise': 440, 'epoll_pwait2': 441, 'mount_setattr': 442, 'quotactl_fd': 443, 'landlock_create_ruleset': 444, 'landlock_add_rule': 445, 'landlock_restrict_self': 446, 'memfd_secret': 447, 'process_mrelease': 448, 'futex_waitv': 449, 'set_mempolicy_home_node': 450, 'cachestat': 451, 'fchmodat2': 452, 'map_shadow_stack': 453, 'futex_wake': 454, 'futex_wait': 455, 'futex_requeue': 456, 'statmount': 457, 'listmount': 458, 'lsm_get_self_attr': 459, 'lsm_set_self_attr': 460, 'lsm_list_modules': 461, 'mseal': 462, 'setxattrat': 463, 'getxattrat': 464, 'listxattrat': 465, 'removexattrat': 466}

_syscall_table_64 = {'read': 0, 'write': 1, 'open': 2, 'close': 3, 'newstat': 4, 'newfstat': 5, 'newlstat': 6, 'poll': 7, 'lseek': 8, 'mmap': 9, 'mprotect': 10, 'munmap': 11, 'brk': 12, 'rt_sigaction': 13, 'rt_sigprocmask': 14, 'rt_sigreturn': 15, 'ioctl': 16, 'pread64': 17, 'pwrite64': 18, 'readv': 19, 'writev': 20, 'access': 21, 'pipe': 22, 'select': 23, 'sched_yield': 24, 'mremap': 25, 'msync': 26, 'mincore': 27, 'madvise': 28, 'shmget': 29, 'shmat': 30, 'shmctl': 31, 'dup': 32, 'dup2': 33, 'pause': 34, 'nanosleep': 35, 'getitimer': 36, 'alarm': 37, 'setitimer': 38, 'getpid': 39, 'sendfile64': 40, 'socket': 41, 'connect': 42, 'accept': 43, 'sendto': 44, 'recvfrom': 45, 'sendmsg': 46, 'recvmsg': 47, 'shutdown': 48, 'bind': 49, 'listen': 50, 'getsockname': 51, 'getpeername': 52, 'socketpair': 53, 'setsockopt': 54, 'getsockopt': 55, 'clone': 56, 'fork': 57, 'vfork': 58, 'execve': 59, 'exit': 60, 'wait4': 61, 'kill': 62, 'newuname': 63, 'semget': 64, 'semop': 65, 'semctl': 66, 'shmdt': 67, 'msgget': 68, 'msgsnd': 69, 'msgrcv': 70, 'msgctl': 71, 'fcntl': 72, 'flock': 73, 'fsync': 74, 'fdatasync': 75, 'truncate': 76, 'ftruncate': 77, 'getdents': 78, 'getcwd': 79, 'chdir': 80, 'fchdir': 81, 'rename': 82, 'mkdir': 83, 'rmdir': 84, 'creat': 85, 'link': 86, 'unlink': 87, 'symlink': 88, 'readlink': 89, 'chmod': 90, 'fchmod': 91, 'chown': 92, 'fchown': 93, 'lchown': 94, 'umask': 95, 'gettimeofday': 96, 'getrlimit': 97, 'getrusage': 98, 'sysinfo': 99, 'times': 100, 'ptrace': 101, 'getuid': 102, 'syslog': 103, 'getgid': 104, 'setuid': 105, 'setgid': 106, 'geteuid': 107, 'getegid': 108, 'setpgid': 109, 'getppid': 110, 'getpgrp': 111, 'setsid': 112, 'setreuid': 113, 'setregid': 114, 'getgroups': 115, 'setgroups': 116, 'setresuid': 117, 'getresuid': 118, 'setresgid': 119, 'getresgid': 120, 'getpgid': 121, 'setfsuid': 122, 'setfsgid': 123, 'getsid': 124, 'capget': 125, 'capset': 126, 'rt_sigpending': 127, 'rt_sigtimedwait': 128, 'rt_sigqueueinfo': 129, 'rt_sigsuspend': 130, 'sigaltstack': 131, 'utime': 132, 'mknod': 133, 'personality': 135, 'ustat': 136, 'statfs': 137, 'fstatfs': 138, 'sysfs': 139, 'getpriority': 140, 'setpriority': 141, 'sched_setparam': 142, 'sched_getparam': 143, 'sched_setscheduler': 144, 'sched_getscheduler': 145, 'sched_get_priority_max': 146, 'sched_get_priority_min': 147, 'sched_rr_get_interval': 148, 'mlock': 149, 'munlock': 150, 'mlockall': 151, 'munlockall': 152, 'vhangup': 153, 'modify_ldt': 154, 'pivot_root': 155, 'ni_syscall': 156, 'prctl': 157, 'arch_prctl': 158, 'adjtimex': 159, 'setrlimit': 160, 'chroot': 161, 'sync': 162, 'acct': 163, 'settimeofday': 164, 'mount': 165, 'umount': 166, 'swapon': 167, 'swapoff': 168, 'reboot': 169, 'sethostname': 170, 'setdomainname': 171, 'iopl': 172, 'ioperm': 173, 'init_module': 175, 'delete_module': 176, 'quotactl': 179, 'gettid': 186, 'readahead': 187, 'setxattr': 188, 'lsetxattr': 189, 'fsetxattr': 190, 'getxattr': 191, 'lgetxattr': 192, 'fgetxattr': 193, 'listxattr': 194, 'llistxattr': 195, 'flistxattr': 196, 'removexattr': 197, 'lremovexattr': 198, 'fremovexattr': 199, 'tkill': 200, 'time': 201, 'futex': 202, 'sched_setaffinity': 203, 'sched_getaffinity': 204, 'io_setup': 206, 'io_destroy': 207, 'io_getevents': 208, 'io_submit': 209, 'io_cancel': 210, 'epoll_create': 213, 'remap_file_pages': 216, 'getdents64': 217, 'set_tid_address': 218, 'restart_syscall': 219, 'semtimedop': 220, 'fadvise64': 221, 'timer_create': 222, 'timer_settime': 223, 'timer_gettime': 224, 'timer_getoverrun': 225, 'timer_delete': 226, 'clock_settime': 227, 'clock_gettime': 228, 'clock_getres': 229, 'clock_nanosleep': 230, 'exit_group': 231, 'epoll_wait': 232, 'epoll_ctl': 233, 'tgkill': 234, 'utimes': 235, 'mbind': 237, 'set_mempolicy': 238, 'get_mempolicy': 239, 'mq_open': 240, 'mq_unlink': 241, 'mq_timedsend': 242, 'mq_timedreceive': 243, 'mq_notify': 244, 'mq_getsetattr': 245, 'kexec_load': 246, 'waitid': 247, 'add_key': 248, 'request_key': 249, 'keyctl': 250, 'ioprio_set': 251, 'ioprio_get': 252, 'inotify_init': 253, 'inotify_add_watch': 254, 'inotify_rm_watch': 255, 'migrate_pages': 256, 'openat': 257, 'mkdirat': 258, 'mknodat': 259, 'fchownat': 260, 'futimesat': 261, 'newfstatat': 262, 'unlinkat': 263, 'renameat': 264, 'linkat': 265, 'symlinkat': 266, 'readlinkat': 267, 'fchmodat': 268, 'faccessat': 269, 'pselect6': 270, 'ppoll': 271, 'unshare': 272, 'set_robust_list': 273, 'get_robust_list': 274, 'splice': 275, 'tee': 276, 'sync_file_range': 277, 'vmsplice': 278, 'move_pages': 279, 'utimensat': 280, 'epoll_pwait': 281, 'signalfd': 282, 'timerfd_create': 283, 'eventfd': 284, 'fallocate': 285, 'timerfd_settime': 286, 'timerfd_gettime': 287, 'accept4': 288, 'signalfd4': 289, 'eventfd2': 290, 'epoll_create1': 291, 'dup3': 292, 'pipe2': 293, 'inotify_init1': 294, 'preadv': 295, 'pwritev': 296, 'rt_tgsigqueueinfo': 297, 'perf_event_open': 298, 'recvmmsg': 299, 'fanotify_init': 300, 'fanotify_mark': 301, 'prlimit64': 302, 'name_to_handle_at': 303, 'open_by_handle_at': 304, 'clock_adjtime': 305, 'syncfs': 306, 'sendmmsg': 307, 'setns': 308, 'getcpu': 309, 'process_vm_readv': 310, 'process_vm_writev': 311, 'kcmp': 312, 'finit_module': 313, 'sched_setattr': 314, 'sched_getattr': 315, 'renameat2': 316, 'seccomp': 317, 'getrandom': 318, 'memfd_create': 319, 'kexec_file_load': 320, 'bpf': 321, 'execveat': 322, 'userfaultfd': 323, 'membarrier': 324, 'mlock2': 325, 'copy_file_range': 326, 'preadv2': 327, 'pwritev2': 328, 'pkey_mprotect': 329, 'pkey_alloc': 330, 'pkey_free': 331, 'statx': 332, 'io_pgetevents': 333, 'rseq': 334, 'uretprobe': 335, 'pidfd_send_signal': 424, 'io_uring_setup': 425, 'io_uring_enter': 426, 'io_uring_register': 427, 'open_tree': 428, 'move_mount': 429, 'fsopen': 430, 'fsconfig': 431, 'fsmount': 432, 'fspick': 433, 'pidfd_open': 434, 'clone3': 435, 'close_range': 436, 'openat2': 437, 'pidfd_getfd': 438, 'faccessat2': 439, 'process_madvise': 440, 'epoll_pwait2': 441, 'mount_setattr': 442, 'quotactl_fd': 443, 'landlock_create_ruleset': 444, 'landlock_add_rule': 445, 'landlock_restrict_self': 446, 'memfd_secret': 447, 'process_mrelease': 448, 'futex_waitv': 449, 'set_mempolicy_home_node': 450, 'cachestat': 451, 'fchmodat2': 452, 'map_shadow_stack': 453, 'futex_wake': 454, 'futex_wait': 455, 'futex_requeue': 456, 'statmount': 457, 'listmount': 458, 'lsm_get_self_attr': 459, 'lsm_set_self_attr': 460, 'lsm_list_modules': 461, 'mseal': 462, 'setxattrat': 463, 'getxattrat': 464, 'listxattrat': 465, 'removexattrat': 466}
