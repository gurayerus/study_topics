# 1. pH and strong acids and bases

AP topics **8.1 Introduction to Acids and Bases** and **8.2 pH and pOH of Strong Acids and Bases**

> **Goal:** Calculate pH, pOH, [H₃O⁺], and [OH⁻] for pure water and for any strong acid or strong base solution.

## Brønsted–Lowry acids and bases

- An **acid** is a proton (H⁺) donor. A **base** is a proton acceptor.
- When an acid gives up its proton, what's left is its **conjugate base**. When a base accepts a proton, it becomes its **conjugate acid**. The two members of a conjugate pair differ by exactly one H⁺.

```
 HF   +  H₂O   ⇌   H₃O⁺   +   F⁻
acid     base      conj.      conj.
                   acid       base
```

- **Amphoteric** species can act as an acid or a base. Water is the main example (it's the base above, and an acid toward NH₃). HCO₃⁻ and H₂PO₄⁻ are amphoteric too.
- H⁺(aq) and H₃O⁺(aq) mean the same thing. The AP exam prefers H₃O⁺ but accepts H⁺.

## Water autoionizes

Even pure water contains a few ions:

```
2 H₂O(l) ⇌ H₃O⁺(aq) + OH⁻(aq)        Kw = [H₃O⁺][OH⁻] = 1.0 × 10⁻¹⁴  (at 25 °C)
```

This holds in **every** aqueous solution, not just pure water. If you know [H₃O⁺], you know [OH⁻]:

```
[OH⁻] = Kw / [H₃O⁺]
```

## pH and pOH

```
pH  = −log[H₃O⁺]          [H₃O⁺] = 10^(−pH)
pOH = −log[OH⁻]           [OH⁻]  = 10^(−pOH)
pH + pOH = 14.00          (at 25 °C)
```

| Solution | At 25 °C |
|---|---|
| acidic | [H₃O⁺] > [OH⁻], pH < 7 |
| neutral | [H₃O⁺] = [OH⁻], pH = 7 |
| basic | [H₃O⁺] < [OH⁻], pH > 7 |

**The scale is logarithmic.** A change of 1 pH unit is a 10× change in [H₃O⁺]. pH 2 is 1000 times more acidic than pH 5, not 2.5 times.

### Neutral doesn't always mean pH 7

Autoionization is endothermic, so **Kw increases with temperature** (Le Châtelier). At 50 °C, Kw ≈ 5.5 × 10⁻¹⁴, so in pure water:

```
[H₃O⁺] = √(5.5 × 10⁻¹⁴) = 2.3 × 10⁻⁷ M   →   pH = 6.63
```

The water is still **neutral** because [H₃O⁺] = [OH⁻]. Neutral means the two concentrations are equal, not that pH = 7. This comes up as a multiple-choice trap.

## Strong acids: memorize these six

| Strong acid | Formula |
|---|---|
| hydrochloric | HCl |
| hydrobromic | HBr |
| hydroiodic | HI |
| perchloric | HClO₄ |
| nitric | HNO₃ |
| sulfuric | H₂SO₄ (first proton only; HSO₄⁻ is a weak acid) |

Strong acids ionize **completely**, so no equilibrium calculation is needed:

```
HNO₃(aq) + H₂O(l) → H₃O⁺(aq) + NO₃⁻(aq)        [H₃O⁺] = [HNO₃]initial
```

## Strong bases: group 1 and group 2 hydroxides

They dissociate completely. Watch the subscript:

```
NaOH(aq)    → Na⁺(aq)  + OH⁻(aq)          [OH⁻] = [NaOH]
Ba(OH)₂(aq) → Ba²⁺(aq) + 2 OH⁻(aq)        [OH⁻] = 2 × [Ba(OH)₂]
```

## Significant figures with logs

The number of **decimal places** in pH equals the number of **significant figures** in the concentration.

- [H₃O⁺] = 0.025 M (2 sig figs) → pH = 1.60 (2 decimal places)
- [H₃O⁺] = 0.0100 M (3 sig figs) → pH = 2.000

The digit before the decimal point in a pH only places the decimal point in the concentration, so it doesn't count as a significant figure.

## Worked examples

**Example 1. What are the pH, pOH, and [OH⁻] of 0.025 M HNO₃?**

HNO₃ is a strong acid, so [H₃O⁺] = 0.025 M.

```
pH    = −log(0.025) = 1.60
pOH   = 14.00 − 1.60 = 12.40
[OH⁻] = 1.0 × 10⁻¹⁴ / 0.025 = 4.0 × 10⁻¹³ M
```

**Example 2. What is the pH of 0.0050 M Ba(OH)₂?**

Each Ba(OH)₂ releases 2 OH⁻, so [OH⁻] = 2 × 0.0050 = 0.010 M.

```
pOH = −log(0.010) = 2.00
pH  = 14.00 − 2.00 = 12.00
```

**Example 3. 10.0 mL of 0.10 M HCl is diluted to 1.00 L. What is the pH?**

First find moles, then the new concentration:

```
mol H₃O⁺ = (0.0100 L)(0.10 mol/L) = 1.0 × 10⁻³ mol
[H₃O⁺]   = 1.0 × 10⁻³ mol / 1.00 L = 1.0 × 10⁻³ M      →   pH = 3.00
```

A 100× dilution raised the pH by exactly 2 units, from 1.00 to 3.00.

**Example 4. A solution has pH 3.45. What is [H₃O⁺]?**

```
[H₃O⁺] = 10^(−3.45) = 3.5 × 10⁻⁴ M
```

## Common mistakes

- **Forgetting the 2 for group 2 hydroxides.** [OH⁻] in 0.010 M Ca(OH)₂ is 0.020 M.
- **Reporting pOH when the question asks for pH**, especially with bases. Finish with pH = 14.00 − pOH.
- **Treating a very dilute strong acid as basic.** For 1.0 × 10⁻⁸ M HCl, −log gives "pH 8", which is impossible for an acid. Water's own 1.0 × 10⁻⁷ M H₃O⁺ dominates, so the pH is slightly below 7 (about 6.98). For concentrations below about 10⁻⁶ M, water's contribution matters.
- **Mixing up "strong" and "concentrated."** Strong describes how completely an acid ionizes. Concentrated describes how much is dissolved. 0.001 M HCl is strong but dilute.

➡️ Next: [practice.md](practice.md)
