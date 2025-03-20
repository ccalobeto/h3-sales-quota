import { feature } from 'topojson-client';

import pe from '$lib/data/peru-100k.json';
import data from '$lib/data/synthetic.csv';

const rawData = data.map((d) => ({
  // generate a geojson file with points
  ...d,
  customer_id: + d.incident_id,
  longitud: + d.longitud,
  latitud: + d.latitud,
  año: + d.año,
  ticket: + parseFloat(d.ticket).toFixed(2)
})).sort((a, b) => a.año - b.año).filter(d => d.año == 2023);

export const geoData = () => {
  // return coords2geo(rawData, {lat: 'latitud', lon: 'longitud'});
  return {
    type: 'FeatureCollection',
    features: rawData.map((d) => ({
      type: 'Feature',
      properties: d,
      geometry: {
        type: 'Point',
        coordinates: [d.longitud, d.latitud]
      }
    }))
  };
}

export const hexagons = () => {
  // Miraflores boundary
	let boundary = feature(pe, pe.objects.level4).features.filter((d) => d.id == '150122');

  boundary.map((d) => {
    d.properties = {
      areacd: d.properties.id,
      areanm: d.properties.name,
    }
  })

  return boundary;
};