# Text Retrieval Engine for Construction Equipment
## Motivation
My employer receives ERP data from major equipment rental companies, aggregates the data, and provides benchmark insights for the industry. One of the biggest challenges in this business model is how to normalize equipment information: the benchmarks are calculated based on client-provided make/model information, but different companies have different representations and conventions of equipment information. In addition, there are countless variations of minor trims in the world of construction equipment. For example, Caterpillar 336 and 336GC are essentially treated as the same model, although there could be a very minor difference.

My proposed system accepts a set of make/model as a query, calculates similarities with the document database, and returns Top N matching results depending on the parameter and score.

This is a course project for [CS410: Text Information Systems](https://courses.engr.illinois.edu/cs410/fa2023/) at [University of Illinois Urbana-Champaign](https://illinois.edu/).

## :point_right: Final Deliverables
1. [Web Demo](https://storage.googleapis.com/my-front/index.html)
2. [API Endpoint](https://my-api-y7vscpfafa-ue.a.run.app/)
3. [API Documentation](https://my-api-y7vscpfafa-ue.a.run.app/docs) (FastAPI)
4. Software Documentation
5. Software Usage Tutorial Presentation

## :point_right: Past Deliverables
1. [Project Proposal](reports/Project%20proposal.pdf) (due Oct 27, 2023)
3. [Project Progress Report](reports/Progress%20report.pdf) (due Nov 21, 2023)

## Tech Stack
* Python 3.11
* FastAPI
* HTML, CSS, JavaScript for frontend
* Docker
* Google Cloud (Clound Run) for deployment

## Team
**Group Name:** Kaz Lone Star :star2:	

**Member:** Kazuhei Sasaki (ksasaki2 AT illinois DOT edu) :snail:
