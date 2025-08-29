import os
import numpy as np
import soundfile as sf

def normalize(x: np.ndarray) -> np.ndarray:
    """Peak normalize to [-1, 1]"""
    peak = np.max(np.abs(x))
    if peak > 0:
        x = x / peak
    return x

def post_processing(x: np.ndarray, fades: bool = True, norm: bool = True) -> np.ndarray:
    # Normalize
    x = normalize(x) if norm else x

    # Set Fades
    if fades:
        fade_in = int(160 * 2)
        fade_out = int(160 * 2.5)

        if x.ndim == 1:
            # mono
            x[:fade_in] *= np.linspace(0, 1, fade_in) ** 0.5
            x[-fade_out:] *= np.linspace(1, 0, fade_out) ** 0.5
        else:
            # multi-channel
            x[:, :fade_in] *= np.linspace(0, 1, fade_in)[None, :] ** 0.5
            x[:, -fade_out:] *= np.linspace(1, 0, fade_out)[None, :] ** 0.5

    return x


def process_folder(folder_path: str):
    for root, _, files in os.walk(folder_path):
        for fname in files:
            if fname.lower().endswith(".wav"):
                in_path = os.path.join(root, fname)

                # Load audio
                waveform, sr = sf.read(in_path, always_2d=False)

                # Apply post-processing
                processed = post_processing(waveform)

                # Save back (overwrite original)
                sf.write(in_path, processed, sr)
                print(f"Processed: {in_path}")


if __name__ == "__main__":
    folder = '/Users/robindoerfler/Documents/Projects/_UPF/Master_Thesis/prce-examples/audiofiles'
    process_folder(folder)
