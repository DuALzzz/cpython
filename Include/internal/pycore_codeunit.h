// pycore_codeunit.h
#ifndef PyCORE_CODEUNIT_H
#define PyCORE_CODEUNIT_H
#include "pycore_backoff.h"     // _Py_BackoffCounter
typedef union {
    uint16_t cache;
    struct {
        uint8_t code;
        uint8_t arg;
    } op;
    _Py_BackoffCounter counter;  // First cache entry of specializable op
} _Py_CODEUNIT;

#endif /* PyCORE_CODEUNIT_H */
