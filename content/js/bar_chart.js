<!-- SINGLE BAR CHART -->
var current_age = 25;
var current_year = 2010;
var current_nodes = 1;
var current_risk = 97.0;

var chart = d3.select(".bar_chart")
  .append("svg")
    .attr("width", 800)
    .attr("height", 100);

var chance_scale = d3.scale.linear()
  .domain([0, 100])
  .range([0, 800]);

var bar = chart.append("g")
               .attr("class", "bar")

bar.append("rect")
  .attr("id", "chancebar")
  .attr("class", "bar")
  .attr("width", chance_scale(current_risk))
  .attr("height", 50);

 bar.append("text")
    .attr("id", "percent_text")
    .attr("dy", ".75em")
    .attr("y", 15)
    .attr("x", chance_scale(current_risk-5))
    .attr("text-anchor", "middle")
    .attr("fill", "white")
    .attr("font-size", 20)
    .text( current_risk.toFixed(1) + "%");


<!-- FUNCTION TO GET CHANCE FROM YOUR PREDICTOR WITH AJAX AND CHANGE BAR  HEIGHT -->
function getAndDrawChance(age, year, nodes){ 
    
    year = year - 1900;
	$.ajax({ 
		type: "POST", 
		contentType: "application/json; charset=utf-8", 
		url: "/score", 
		dataType: "json", 
		async: true, 
		data: "{\"example\": ["+age+","+year+","+nodes+"]}", 
		success: function (data) { 
		   var chance = 100 * data["score"]; 
               d3.select("#chancebar")
                     .attr("width", chance_scale(chance));
               d3.select("#percent_text")
                     .attr("x", chance_scale(chance-5))
                     .text(chance.toFixed(1) + "%");
		}, 
		error: function (result) { 
		} 
	       }) 
} 


<!-- SLIDERS -->

d3.select('#age_slider')
  .call(
        d3.slider()
          .value(current_age)
          .step(1)
          .axis(true)
          .on("slide", function(evt,value) {
                                            d3.select('#age').text(value);
                                            current_age = value;
                                            getAndDrawChance(current_age, current_year, current_nodes)
                                           }
             )
       );

d3.select('#year_slider')
  .call(
        d3.slider()
          .value(current_year)
          .min(1950)
          .max(2010)
          .step(1)
          .axis(true)
          .on("slide", function(evt,value) {
                                             d3.select('#year').text(value);
                                             current_year = value;
                                             getAndDrawChance(current_age, current_year, current_nodes)
                                           }
             )
       );

d3.select('#nodes_slider')
  .call(
        d3.slider()
          .value(current_nodes)
          .max(40)
          .step(1)
          .axis(true)
          .on("slide", function(evt,value) {
                                             d3.select('#nodes').text(value);
                                             current_nodes = value;
                                             getAndDrawChance(current_age, current_year, current_nodes)
                                           }
             )
       );

