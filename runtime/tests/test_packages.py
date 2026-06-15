import importlib
import subprocess

import pytest

packages = [
    "accelerate",
    "datasets",
    "einops",
    "gensim",
    "langchain_community",
    "langchain",
    "loguru",
    "numpy",
    "pandas",
    "peft",
    "scipy",
    "sentence_transformers",
    "sklearn",
    "spacy",
    "timm",
    "torch",
    "transformers",
    "vllm",
]


def is_gpu_available():
    try:
        return subprocess.check_call(["nvidia-smi"]) == 0

    except FileNotFoundError:
        return False


GPU_AVAILABLE = is_gpu_available()


@pytest.mark.parametrize("package_name", packages, ids=packages)
def test_import(package_name):
    """Test that certain dependencies are importable."""
    importlib.import_module(package_name)


@pytest.mark.skipif(not GPU_AVAILABLE, reason="No GPU available")
def test_torch_cuda_available():
    """Test that PyTorch can see CUDA."""
    import torch

    assert torch.cuda.is_available(), "CUDA should be available"


@pytest.mark.skipif(not GPU_AVAILABLE, reason="No GPU available")
def test_torch_allocate_tensor():
    """Test that PyTorch can allocate a tensor on GPU."""
    import torch

    tensor = torch.zeros(1).cuda()
    assert tensor.device.type == "cuda"


@pytest.mark.skipif(not GPU_AVAILABLE, reason="No GPU available")
def test_cupy_allocate_array():
    """Test that CuPy can allocate an array on GPU."""
    import cupy as cp

    arr = cp.array([1, 2, 3, 4, 5, 6])
    assert arr.device.id >= 0


def test_spacy():
    import spacy
    from spacy.tokens import DocBin

    if GPU_AVAILABLE:
        spacy.require_gpu()

    nlp = spacy.blank("en")
    training_data = [
        ("Tokyo Tower is 333m tall.", [(0, 11, "BUILDING")]),
    ]

    # the DocBin will store the example documents
    db = DocBin()
    for text, annotations in training_data:
        doc = nlp(text)
        ents = []
        for start, end, label in annotations:
            span = doc.char_span(start, end, label=label)
            ents.append(span)
        doc.ents = ents
        db.add(doc)


@pytest.mark.skipif(not GPU_AVAILABLE, reason="No GPU available")
def test_vllm_imports():
    """Test that vLLM core classes can be imported (requires GPU)."""
    from vllm import LLM, SamplingParams

    assert LLM is not None
    assert SamplingParams is not None
