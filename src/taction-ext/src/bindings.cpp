#include <pybind11/pybind11.h>
#include <taction/main.hpp>

namespace py = pybind11;

namespace taction {

PYBIND11_MODULE(_taction_ext, m) {
  bind_add(m);
  bind_arange(m);
}

}  // namespace taction
