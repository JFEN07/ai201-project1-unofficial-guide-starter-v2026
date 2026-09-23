"""
Stage 2 of the pipeline: splitting documents into chunks.

⚠️ THIS IS THE FILE YOU CHANGE IN MILESTONE 3.

`split_documents` below is deliberately plain. It cuts every document into
fixed-size pieces with a fixed overlap and pays no attention to where sentences
or paragraphs end. It works, and it is not good.

On a corpus of short posts it may not cut anything at all: `campus_life` comes
out as 88 documents and 88 chunks, because almost nothing in it reaches 800
characters. That is the baseline, not a bug — Milestone 3 is where you decide
whether one post should stay one chunk.

Your job in Milestone 3 is to replace the *body* of `split_documents` with a
strategy that fits the documents you actually read in Milestone 1. Keep the
name and the shape of what it returns — the rest of the pipeline calls it, and
your README has to name the function that produced your chunks.

If you get stuck for 30 minutes, `fallback_split` is the original. Switch back
to it, write down what you saw, and move on. That's a real observation about
your pipeline, not giving up.
"""

from dataclasses import dataclass

import config
from ingest import Document


@dataclass
class Chunk:
    """One piece of one document."""

    text: str
    source: str        # which file it came from
    index: int         # which chunk within that file, starting at 0
    produced_by: str   # the function that made it — cite this in your README

    @property
    def label(self) -> str:
        return f"{self.source}#{self.index}"


def fallback_split(
    documents: list[Document],
    chunk_size: int | None = None,
    overlap: int | None = None,
) -> list[Chunk]:
    """
    The starter's original chunker. Fixed-size character windows with overlap.

    Keep this function. Milestone 3's stop rule points back at it, and having
    something to compare your own strategy against is useful in unit 2.
    """
    chunk_size = chunk_size or config.CHUNK_SIZE
    overlap = overlap or config.CHUNK_OVERLAP

    if overlap >= chunk_size:
        raise ValueError("overlap has to be smaller than chunk_size")

    chunks: list[Chunk] = []
    for doc in documents:
        start = 0
        index = 0
        while start < len(doc.text):
            piece = doc.text[start : start + chunk_size].strip()
            if piece:
                chunks.append(
                    Chunk(
                        text=piece,
                        source=doc.source,
                        index=index,
                        produced_by="chunker.py::fallback_split",
                    )
                )
                index += 1
            start += chunk_size - overlap

    return chunks

# My chunking function that splits on paragraph breaks
def split_documents(
    documents: list[Document],
    chunk_size: int | None = None,
    overlap: int | None = None,
) -> list[Chunk]:
    """
    The starter's original chunker. Fixed-size character windows with overlap.

    Keep this function. Milestone 3's stop rule points back at it, and having
    something to compare your own strategy against is useful in unit 2.
    """
    chunk_size = chunk_size or config.CHUNK_SIZE
    overlap = overlap or config.CHUNK_OVERLAP

    if overlap >= chunk_size:
        raise ValueError("overlap has to be smaller than chunk_size")

    chunks: list[Chunk] = []
    for doc in documents:

        # Separates documents into paragraphs and stores them in a list
        # Also removes empty "paragraphs"
        paragraphs = [
            paragraph.strip()
            for paragraph in doc.text.split("\n\n")
            if paragraph.strip()
        ]
        
        # Aqcuires the title of each document
        title = next(
            (p.lstrip("# ").strip() for p in paragraphs if p.startswith("# ")),
            doc.source.rsplit("/", 1)[-1].rsplit(".", 1)[0].replace("_", " "),
        )

        pieces: list[str] = []
        current_paragraphs: list[str] = []
        last_heading: str | None = None

        for paragraph in paragraphs:

            # Checks if document title has changed
            if paragraph.lstrip().startswith("#") and "\n" not in paragraph:
                last_heading = paragraph

            # Temporarily add paragraph with space to the current chunk.
            current_paragraphs.append(paragraph)
            candidate = "\n\n".join(current_paragraphs)

            # Removes overflowing paragraph if the chunk is too long
            if len(candidate) > chunk_size and len(current_paragraphs) > 1:
                overflowing_paragraph = current_paragraphs.pop()

                # Carries a heading that ends a chunk to the next chunk
                carried: list[str] = []
                while (
                    len(current_paragraphs) > 1
                    and current_paragraphs[-1].lstrip().startswith("#")
                    and "\n" not in current_paragraphs[-1]
                ):
                    carried.insert(0, current_paragraphs.pop())

                pieces.append("\n\n".join(current_paragraphs))

                if (
                    not carried
                    and not overflowing_paragraph.lstrip().startswith("#")
                    and last_heading
                ):
                    carried = [last_heading]

                # Only overlap body text when no heading was carried.
                if not carried and len(current_paragraphs[-1]) <= overlap:
                    carried = [current_paragraphs[-1]]

                current_paragraphs = carried + [overflowing_paragraph]

                # Drop the overlap if its addition surpasses chunk_size
                if len("\n\n".join(current_paragraphs)) > chunk_size:
                    current_paragraphs = [overflowing_paragraph]

        # Save the final unfinished chunk.
        if current_paragraphs:
            tail = "\n\n".join(current_paragraphs)
            if pieces and len(tail) < chunk_size // 4:
                pieces[-1] = pieces[-1] + "\n\n" + tail
            else:
                pieces.append(tail)

        # Convert each text piece into a Chunk object.
        for index, piece in enumerate(pieces):

            # Title added to start unless a title is already there
            text = (
                piece
                if piece.lstrip().startswith("# ")
                else f"# {title}\n\n{piece}"
            )

            chunks.append(
                Chunk(
                    text=piece,
                    source=doc.source,
                    index=index,
                    produced_by="chunker.py::split_documents",
                )
            )

    return chunks    


    """
    Split documents into chunks. ⚠️ REPLACE THE BODY OF THIS IN MILESTONE 3.

    Right now it just calls the fallback. That is the plain, generic behaviour
    the brief is talking about.

    When you write your own strategy, set `produced_by` to
    "chunker.py::split_documents" so your README's Sample Chunks section names
    the right function. `app.py chunks` prints that string for you.

    Things worth thinking about before you write any code:
      - Are your documents short posts or long guides?
      * Documents are long guides so a large chunk size is preferred.
      - Is the useful information in one sentence, or spread over a paragraph?
      - Would splitting on paragraph breaks keep more thoughts intact than
        splitting on a character count?
      * The useful information in city_guides documents are spread over 
	paragraphs and would benefit from adjusted rather than static chunk 
	splitting, specifically splitting at multiple paragraph breaks to
	ideally keep headers and paragraphs together.
      + To document, I originally used a chunk size of 800 and overlap of 100, 
	which cause the documents to be split across 3 chunks at times with 
	no reference to the town that their information pertained to, outside 
	of the first chunks of the documents.
    """
    return fallback_split(documents)


def describe(chunks: list[Chunk]) -> str:
    """A one-line summary, printed after indexing."""
    if not chunks:
        return "0 chunks"
    lengths = [len(c.text) for c in chunks]
    return (
        f"{len(chunks)} chunks, "
        f"{sum(lengths) // len(lengths)} characters on average "
        f"(shortest {min(lengths)}, longest {max(lengths)}), "
        f"produced by {chunks[0].produced_by}"
    )


if __name__ == "__main__":
    from ingest import load_documents

    chunks = split_documents(load_documents())
    print(describe(chunks))
