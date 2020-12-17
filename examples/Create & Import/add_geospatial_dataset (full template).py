import pynada as nada
import inspect

nada.set_api_url('http://training.ihsn.org/index.php/api/')
api_key = 'cf16a23a3cfc6a928f63dd3c8daf8796'
nada.set_api_key(api_key)

##################################
# add_geospatial_dataset template
##################################

dataset_id = "GEOSPATIAL_DATASET_SAMPLE_01"
repository_id = "central"
published = 0
overwrite = "yes"
metadata_maintenance = {
	"update_frequency": "maintenance update_frequency",
	"note": "maintenance note",
	"contact": [
		{
			"person_name": "maintenance contact person_name",
			"role": "maintenance contact role",
			"organisation": "maintenance contact organisation",
			"position": "maintenance contact position",
			"instructions": "maintenance contact instruction",
			"phone": "maintenance contact phone",
			"fax": "maintenance contact fax",
			"email": "maintenance contact email",
			"website": "maintenance contact website",
			"address": "maintenance contact address",
			"city": "maintenance contact city",
			"administrative_area": "maintenance contact administrative_area",
			"postal_code": "maintenance contact postal_code",
			"country": "maintenance contact country"
		}
	],
	"prod_date": "2020-12-31",
	"version": "the current version of the dataset"
}
dataset_description = {
	"file_identifier": "GEOSPATIAL_DATASET_SAMPLE_01",
	"language": "language code",
	"charset_code": "UTF-8",  # character encoding used
	"hierarchy_level": "geospatial dataset hierarchy_level",
	"date_stamp": "2009-11-17T10:00:00",
	"contact": [
		{
			"person_name": "contact person_name",
			"role": "contact role",
			"organisation": "contact organisation",
			"position": "contact position",
			"instructions": "contact instruction",
			"phone": "contact phone",
			"fax": "contact fax",
			"email": "contact email",
			"website": "contact website",
			"address": "contact address",
			"city": "contact city",
			"administrative_area": "contact administrative_area",
			"postal_code": "contact postal_code",
			"country": "contact country"
		}
	],
	"identification_info": {
		"title": "[Template] Geospatial Dataset Sample 01",
		"alternate_title": "Geospatial Dataset Sample 01 (alternate_title)",
		"date": [
			{
				"date": "2020-12-31",
				"type": "type of event e.g. publication"
			}
		],
		"edition": "Edition e.g. first",
		"identifiers": [
			{
				"identifier": "geospatial data identifier"
			}
		],
		"presentation_form": "e.g. documentDigital",
		"abstract": inspect.cleandoc("""\
		
			Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce vel ante venenatis, dictum leo in, eleifend lectus. Fusce blandit at nisl eu pellentesque. Curabitur massa ante, rutrum vitae nibh nec, volutpat dignissim urna. 
			Aliquam luctus dolor sem, ac accumsan sapien elementum a. Aenean porttitor vel turpis ac consectetur. 
			Nulla eget lacinia leo, at rutrum nibh. Phasellus vestibulum, lorem in ullamcorper lacinia, neque tellus convallis est, 
			non elementum lorem nisl quis augue. Aenean lobortis augue et massa interdum faucibus. Vivamus mattis imperdiet urna, 
			sit amet tempus eros tristique eu. Morbi ultrices mauris dignissim lacus dapibus efficitur. 
			
		"""),
		"purpose": inspect.cleandoc("""\
		
			Pellentesque elementum massa mauris, ac tincidunt orci scelerisque nec. Sed mattis mauris sed dolor elementum, eget facilisis purus aliquet. Praesent eget iaculis augue, vel elementum purus. 
			Proin aliquam eleifend urna, ut rhoncus neque semper in. Integer a viverra tellus, quis tincidunt sem. Fusce nulla dui, commodo sit amet sem id, mattis eleifend lectus. Suspendisse eget tempus tortor. In quis cursus nulla.
			
		"""),
		"credit": inspect.cleandoc("""\
		
			In posuere tempus mi, in vehicula mi tristique nec. Phasellus neque ipsum, ultrices in interdum eget, vehicula id quam. Aliquam cursus euismod maximus.
						
		"""),
		"status": "status code e.g. historicalArchive",
		"point_of_contact": [
			{
				"person_name": "point_of_contact person_name",
				"role": "point_of_contact role",
				"organisation": "point_of_contact organisation",
				"position": "point_of_contact position",
				"instructions": "point_of_contact instruction",
				"phone": "point_of_contact phone",
				"fax": "point_of_contact fax",
				"email": "point_of_contact@example.org",
				"website": "http://example.org/dataset_description/point_of_contact/website",
				"address": "point_of_contact address",
				"city": "point_of_contact city",
				"administrative_area": "point_of_contact administrative_area",
				"postal_code": "point_of_contact postal_code",
				"country": "point_of_contact country"
			}
		],
		"resource_maintenance": {
			"maintenance_frequency": "maintenance frequency code e.g. weekly"
		},
		"graphic_overview": [
			{
				"name": "graphic_overview name",
				"type": "graphic_overview type",
				"description": "graphic_overview description"
			}
		],
		"keywords": [
			{
				"keyword": "keyword",
				"code": "discipline",  # allowed {discipline, place, stratum, temporal, theme}
				"code_uri": "http://example.org/dataset_description/keyword/lcode_uri"
			}
		],
		"resource_constraints": {
			"legal_constraints": [
				{
					"code_list_uri": "http://example.org/dataset_description/resource_constraints/legal_constraints/code_list_uri",
					"code": "legal_constraints code",
					"value": "legal_constraints value"
				}
			],
			"use_limitations": "use_limitations",
			"other_constraints": "other_constraints"
		},
		"spatial_representation_type": "vector",  # Spatial Representation type - vector, grid, textTable, tin, stereoModel, video
		"representative_fraction_denominator": "100000",  # Spatial Resolution Fraction
		"language": "identification_info language",
		"charset_code": "identification_info charset_code",
		"topics": [
			{
				"topic": "geospatial dataset topic",  # Topic code e.g. farming, biota, boundaries, climatologyMeterologyAtmosphere, economy
				"vocab": "geospatial dataset topic vocab",
				"vocab_uri": "http://example.org/dataset_description/topics/vocab_uri"
			}
		],
		"extent": {
			"geographic_bounding_box": [
				{
					"south": 0,
					"west": 30,
					"north": 20,
					"east": 0
				}
			]
		},
		"supplemental_information": "supplemental_information"
	},
	"distribution_info": {
		"distributors": [
			{
				"person_name": "distributor person_name",
				"role": "distributor role",
				"organisation": "distributor organisation",
				"position": "distributor position",
				"instructions": "distributor instructions",
				"phone": "distributor phone",
				"fax": "distributor fax",
				"email": "distributor.email@example.org",
				"website": "distributor website",
				"address": "distributor address",
				"city": "distributor city",
				"administrative_area": "distributor administrative_area",
				"postal_code": "distributor postal_code",
				"country": "distributor country"
			}
		],
		"online_resource": [
			{
				"url": "http://example.org/dataset_description/distribution_info/online_resource",
				"name": "distribution_info online_resource name",
				"description": "distribution_info online_resource description",
				"format": "CSV"  # distribution_info online_resource file format e.g. CSV, ZIP
			}
		]
	},
	"data_quality_info": {
		"Scope": "data_quality_info scope",
		"lineage": "data_quality_info lineage statement"
	},
	"spatial_representation_info": {
		"topology_level": "geometryOnly",  # Topology Level Code: {geometryOnly, topology1D, planarGraph, fullPlanarGraph, surfaceGraph, fullSurfaceGraph, topology3D, fullTopology3D, abstract}
		"Geometric_object_code": "complex"  # Geometric Object Type Code codes ={complex, composite, curve, point, solid, surface}
	},
	"reference_system_info": {
		"code": "EPSG:5701",  # reference_system Identifier Code
		"code_space": "urn:ogc:def:crs"  # spatial reference system code_space
	}
}
additional = {
	"additional": "additional info"
}

response = nada.add_geospatial_dataset(
	dataset_id=dataset_id,
	repository_id=repository_id,
	published=published,
	overwrite=overwrite,
	metadata_maintenance=metadata_maintenance,
	dataset_description=dataset_description,
	additional=additional
)

print(response)

thumbnail_path = nada.text_to_thumbnail("Geospatial\nDataset")
nada.add_thumbnail(dataset_id, thumbnail_path)