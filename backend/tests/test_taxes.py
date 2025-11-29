from app.services.taxes import irpf_alquiler, plusvalia_venta

def test_irpf_basic():
    impuesto = irpf_alquiler(12000)
    assert impuesto >= 0

def test_plusvalia():
    imp = plusvalia_venta(100000, 150000)
    assert imp == round((150000-100000) * 0.19, 2)
