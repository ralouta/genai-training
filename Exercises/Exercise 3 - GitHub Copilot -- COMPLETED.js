/**

Enhancing Pop-ups with ArcGIS Arcade and GitHub Copilot 

In this exercise, we'll use GitHub Copilot to generate ArcGIS Arcade scripts that customize the content and formatting of pop-ups in ArcGIS Online or ArcGIS Pro. This will demonstrate how Copilot can assist in writing expressions to display dynamic content, perform calculations, and enhance user interaction.

**/

// Calculate the population density and format it with commas
// item id of ACS Layer : f430d25bf03744edbb1579e18c4bf6b8
// total populatio field: B01001_001E
// land area field: ALAND
var pop = $feature.B01001_001E;
var area = $feature.ALAND;
// convert meters to miles
area = area / 2589988;
var density = Round(pop / area, 2);
// Format the density with commas
var formattedDensity = Text(density, "#,###.00");
// Create the content for the pop-up
var popupContent =
  "Population Density: " + formattedDensity + " people per square mile";

return {
  type: "text",
  text: popupContent,
};
