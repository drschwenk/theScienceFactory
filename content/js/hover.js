
// Set up the plot window.
var margin = 80;
var w = 1000 - 2 * margin, h = 700 - 2 * margin;
var svg = d3.select(".plot").append("svg")
                .attr("width", w + 2 * margin)
                .attr("height", h + 2 * margin)
            .append("g")
                .attr("transform", "translate(" + margin + ", " + margin + ")");

// The colorbar.
var color = d3.scale.quantize()
              .range(["#156b87", "#876315", "#543510", "#872815"])
              .domain([0, 1]);

// Axes scaling functions.
var xscale = d3.scale.linear().range([0, w]);
var yscale = d3.scale.linear().range([h, 0]);

// The axes objects themselves.
var xaxis = d3.svg.axis().scale(xscale).ticks(8);
var yaxis = d3.svg.axis().scale(yscale).ticks(8).orient("left");

svg.append("g").attr("class", "x axis")
                   .attr("transform", "translate(0, " + h + ")");
svg.append("g").attr("class", "y axis");

// Show the information about a particular point.
var show_info = function (d) {
    d3.select("#point-info").text(d.new_title
        + " grossed $" + d.act_gross.toFixed(0) + " million");
};

var getdata = function (data) {
    // Rescale the axes.
    xscale.domain([0 - 0.05,
                   d3.max(data, function (d) { return d.prev_gross; }) + 0.05]);
    yscale.domain([0 - 0.05,
                   d3.max(data, function (d) { return d.prev_gross; }) + 0.05]);


    // Display the axes.
    svg.select(".x.axis").call(xaxis);
    svg.select(".y.axis").call(yaxis);

    svg.select(".x.axis").append("text")
        .text("Average previous gross ($100s of millions)").attr("x", (w / 2) - margin*2)
        .attr("y", margin / 1.3);

    svg.select(".x.axis").append("text")
        .text("Third film gross ($100s of millions)").attr("x", (w / 2) - margin*2)
        .attr("transform", "rotate (-90, -50, 0) translate(-200)");

    // Insert the data points.
    svg.selectAll("circle").data(data).enter()
        .append("circle")
            .attr("id", function (d) { return d.new_title; })
            .attr("cx", function (d) { return xscale(d.prev_gross); })
            .attr("cy", function (d) { return yscale(d.act_gross); })
            .attr("r", function (d) { return 3; })
            .style("fill", "deepskyblue")
            .on("mouseover", show_info);
};

d3.json("/data", getdata);

svg.append('line')
    .attr('x1',function (d) { return xscale(0); })
    .attr('x2',function (d) { return xscale(1); })
    .attr('y1',function (d) { return yscale(0); })
    .attr('y2',function (d) { return yscale(1); })
    .style("stroke-dasharray", ("3, 5"))
    .style("stroke-opacity", 0.8)
    .style("stroke", "red");

