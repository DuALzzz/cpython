                int result = _PyExternal_TrySpecialize(next_instr,&stack_pointer,(_PyCache *)cache);
                if(result){
                    oparg = next_instr->op.arg;
                }