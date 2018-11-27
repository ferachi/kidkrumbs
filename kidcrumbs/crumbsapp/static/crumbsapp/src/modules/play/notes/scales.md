# SCALES

Scales are used to map certain dimensions to other representations. This could be a numeric range to some other output
be it numeric or strings. In d3 a domain represents the input to be transformed and the range; the range output.

## Continous Scales
Continuous scales map a continuous, quantitative input domain to a continuous output range. D3js does not construct
these scales directly but can be found in a *linear, power, log, identity, time or sequential color* scale.
some important methods include *domain, range, rangeRound, interpolate, clamp, invert, ticks, tickFormat, nice and
copy*.

Usually their domain takes in an array of 2 values (but 3 is ok and will perform piecewise interpolation if the range is
also 3) and this is same with the range.
With continuous.ticks(), one can get the interval within the range of outputs. One can equally specify the number by
continuous.ticks([count])

interpolate() is used to set the range interpolate factory. This comes in handy during color interpolations.

## Sequential and Diverging Scales
Sequential scales, like diverging scales, are similar to continuous scales in that they map a continuous, numeric input
domain to a continuous output range. However, unlike continuous scales, the output range of a sequential scale is fixed
by its interpolator and not configurable. These scales do not expose invert, range, rangeRound and interpolate methods.
(same as diverging scales)

    d3.scaleSequential(d3.interpolateRainbow)
    d3.scaleDiverging(d3.interpolateSpectral)

## Quantized Scales
These are similar to linear scales except that the use a discrete rather than continuous range. The continuous input
domain is divided into uniform segments based on the number of values in (i.e., the cardinality of) the output range.

    var color = d3.scaleQuantize()
        .domain([0, 1])
            .range(["brown", "steelblue"]);

        color(0.49); // "brown"
        color(0.51); // "steelblue"

    var width = d3.scaleQuantize()
        .domain([10, 100])
            .range([1, 2, 4]);

        width(20); // 1
        width(50); // 2
        width(80); // 4

like continous, the also have an invert called invertExtent, where you can check out the value for the range in the
domain.

    var width = d3.scaleQuantize()
        .domain([10, 100])
            .range([1, 2, 4]);

        width.invertExtent(2); // [40, 70]

## Quantile Scales
Quantile scales map a sampled input domain to a discrete range. The domain is considered continuous and thus the scale
will accept any reasonable input value; however, the domain is specified as a discrete set of sample values. The number
of values in (the cardinality of) the output range determines the number of quantiles that will be computed from the
domain. That is quantile is like quantized except that its domain uses discrete set of sample values.
As an example Quantile scales will be good for checking what grades to assign to a score


## Ordinal Scales
Unlike continuous scales, ordinal scales have a discrete domain and range. For example, an ordinal scale might map a set
of named categories to a set of colors, or determine the horizontal positions of columns in a column chart.

note the diff between an ordinal scale and a quantile scale is that in ordinal scales, you can't select a value not in
the domain. Typically ordinal scales are for categorical data. 

If the given value is not in the scale’s domain, returns the unknown; or, if the unknown value is implicit (the
default), then the value is implicitly added to the domain and the next-available value in the range is assigned to
value, such that this and subsequent invocations of the scale given the same input value return the same output value.

## Band Scales 
These are like ordinal scales (i.e their input must correspond to values in the domain, typically categorical data),
however the output range is continous and numeric. Discrete output values are automatically computed by the scale by
dividing the continuous range into uniform bands. Band scales are typically used for bar charts with an ordinal or
categorical dimension. The unknown value of a band scale is effectively undefined: they do not allow implicit domain
construction.
The diff between a band scale and quantile scale is that the domain is categorical for band scales, not continous.
also the output is continous and not 'somewhat' discrete as in Quantile

    d3.scaleBand()
    band(value) // Given a value in the input domain, returns the start of the corresponding band derived from the output
                // range. If the given value is not in the scale’s domain, returns undefined.


