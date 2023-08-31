
## Introduction

Annocoda is a web app that uses [IIIF](https://iiif.io/) standards to provide image search capabilities. 

More explicitly it uses the [IIIF Content Search 2.0 API](https://iiif.io/api/search/2.0/) to match [web annotations](https://www.w3.org/TR/annotation-model/) with their corresponding images described within a [Presentation API 3.0](https://iiif.io/api/presentation/3.0/) manifest or collection.

## Example

You can select annotations to see where in the image they are located.

![screenshot](./assets/screenshot.png)

## Demo

Current builds are deployed [here](https://annocoda.onrender.com/).

## Requirements

To use the service you need a IIIF manifest which [references a search service](https://iiif.io/api/search/2.0/#3-declaring-services). 

If you want to experiment with your own search service you can try [annotass](https://github.com/jptmoore/annotass).

## Status

Please raise GitHub issues for bugs or feature requests to help support the work.