// pycore_codeunit.h
#ifndef PyCORE_CODEUNIT_H
#define PyCORE_CODEUNIT_H

#ifdef __cplusplus
extern "C" {
#endif

#include <stdint.h>

typedef struct {
    union {
        struct {
            uint16_t backoff : 4;
            uint16_t value : 12;
        };
        uint16_t as_counter;  // For printf("%#x", ...)
    };
} _Py_BackoffCounter;

typedef union {
    uint16_t cache;
    struct {
        uint8_t code;
        uint8_t arg;
    } op;
    _Py_BackoffCounter counter;  // First cache entry of specializable op
} _Py_CODEUNIT;

#ifdef __cplusplus
}
#endif
#endif /* PyCORE_CODEUNIT_H */
