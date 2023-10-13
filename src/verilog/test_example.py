import cocotb
from cocotb.triggers import FallingEdge, RisingEdge, Timer


@cocotb.test()
async def test_example(dut):
    dut.a.value = 0
    dut.b.value = 0
    await Timer(1, units="ns")
    assert dut.c.value == 0

    dut.a.value = 0
    dut.b.value = 1
    await Timer(1, units="ns")
    assert dut.c.value == 0

    dut.a.value = 1
    dut.b.value = 1
    await RisingEdge(dut.c)
    assert dut.c.value == 1

    dut.a.value = 1
    dut.b.value = 0
    await FallingEdge(dut.c)
    assert dut.c.value == 0
