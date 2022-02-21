# Here's my sample title

This is some sample text.

(section-label)=
## Here's my first section

Here is a [reference to the intro](intro.md). Here is a reference to [](section-label).


We can estimate the mass of Jupiter from the period and size of an object orbiting it. For example, we can use Jupiter's moon Callisto to estimate it's mass.

Callisto's period: $p_{c}=16.7 days$

Callisto's orbit radius: $r_{c}=1,900,000 km$

### Now, using [Kepler's Law](https://solarsystem.nasa.gov/resources/310/orbits-and-keplers-laws/) we can work out the mass of Jupiter.

```{math}
:label: eq1
m_{j} \approx \frac{r_{c}}{p_{c}} \times 7.9 \times 10^{10}
```

```{math}
:label: eq2
m_{j} \approx 1.9 \times 10^{27} kg
```

```{margin} Did you know?
Jupiter is 11.0x larger than Earth!
```

```{hint}
NASA provides a lot more information about the physical characteristics of Jupiter [here](https://solarsystem.nasa.gov/planets/jupiter/by-the-numbers/).
```

There might even be more planets out there with a similar mass to Jupiter {cite}`mayor1995jupiter,guillot1999interiors`!

## Bibliography

```{bibliography} references.bib
```