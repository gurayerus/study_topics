# 6. pH, pKa, and indicators

AP topic **8.7 pH and pKa**

> **Goal:** Given a solution's pH and an acid's pKa, say which form (HA or A⁻) is present in greater amount, and by about how much. Choose the right indicator for a titration.

## The rule

Compare the **pH of the solution** with the **pKa of the acid**:

| Condition | What's present in greater amount |
|---|---|
| pH < pKa | **acid form, HA** (protonated) |
| pH = pKa | **equal**, [HA] = [A⁻] |
| pH > pKa | **base form, A⁻** (deprotonated) |

**Memory aid:** when there's a lot of H⁺ around (low pH), the acid keeps its proton.

## How lopsided is it?

Rearranging Henderson–Hasselbalch gives the ratio directly:

```
[A⁻] / [HA] = 10^(pH − pKa)
```

| pH − pKa | [A⁻] : [HA] |
|---|---|
| −2 | 1 : 100 |
| −1 | 1 : 10 |
| 0 | 1 : 1 |
| +1 | 10 : 1 |
| +2 | 100 : 1 |

Each pH unit away from pKa is another factor of 10.

**Example 1.** Acetic acid (pKa = 4.74) is in a solution at pH 6.00. Which form dominates, and by how much?

pH > pKa, so **CH₃COO⁻ dominates**.

```
[CH₃COO⁻] / [CH₃COOH] = 10^(6.00 − 4.74) = 10^1.26 = 18
```

There's about 18 times more acetate than acetic acid.

**Example 2 (biology).** Aspirin is a weak acid with pKa ≈ 3.5. In the stomach (pH ≈ 2), which form dominates?

pH < pKa, so the **un-ionized HA form dominates**, with [HA]/[A⁻] = 10^(3.5 − 2.0) ≈ 32. Neutral molecules cross cell membranes more easily than ions, which is one reason aspirin is absorbed partly in the stomach.

## Polyprotic acids: one pKa per proton

Phosphoric acid has three pKa values: pKa₁ = 2.15, pKa₂ = 7.20, pKa₃ = 12.35.

```
pH:  0 ──── 2.15 ──────── 7.20 ──────── 12.35 ──── 14
       H₃PO₄  |   H₂PO₄⁻    |   HPO₄²⁻    |   PO₄³⁻
```

At any pH, the form between the two nearest pKa values dominates. At pH 7.4 (blood), H₂PO₄⁻ and HPO₄²⁻ are both present, with slightly more HPO₄²⁻.

## Indicators

An acid–base indicator is a **weak acid whose HIn and In⁻ forms have different colors**:

```
HIn(aq) + H₂O(l) ⇌ H₃O⁺(aq) + In⁻(aq)
  color 1                       color 2
```

- pH < pKa(HIn): you see the HIn color.
- pH > pKa(HIn): you see the In⁻ color.
- The color change happens over roughly **pKa ± 1**.

| Indicator | pKa (approx.) | Color change range | Color change (acid → base) |
|---|---|---|---|
| methyl orange | 3.5 | 3.1 – 4.4 | red → yellow |
| methyl red | 5.0 | 4.4 – 6.2 | red → yellow |
| bromothymol blue | 7.1 | 6.0 – 7.6 | yellow → blue |
| phenolphthalein | 9.4 | 8.2 – 10.0 | colorless → pink |

You don't need to memorize these. The exam gives you the table.

### Choosing an indicator

**Pick an indicator whose pKa is close to the pH at the equivalence point.** Then the color change (the endpoint) happens on the steep part of the curve, at nearly the same volume as the equivalence point.

| Titration | Equivalence pH | Good choice |
|---|---|---|
| strong acid + strong base | 7.00 | bromothymol blue. Phenolphthalein also works because the jump is huge. |
| weak acid + strong base | > 7 (e.g., 8.72) | **phenolphthalein** |
| weak base + strong acid | < 7 (e.g., 5.28) | **methyl red** |

To justify a choice, cite both numbers: "Phenolphthalein, because its pKa (about 9.4) is close to the equivalence-point pH of 8.72, so its color changes on the steep part of the curve."

## Lab connection

This topic's skill is reading data from lab setups, often a pH meter reading or the color of an indicator. Expect questions like: *"A drop of bromothymol blue turns the solution blue. What can you conclude about the pH?"* (Answer: the pH is above about 7.6.)

## Common mistakes

- **Flipping the rule.** Low pH means the protonated form (HA) dominates.
- **Picking an indicator by name instead of by pKa.** Always compare the pKa with the equivalence-point pH.
- **Thinking an indicator changes color at pH 7.** It changes near its own pKa.
- **Assuming "dominant" means "only."** At pH = pKa + 1, there's still 1 HA for every 10 A⁻.

➡️ Next: [practice.md](practice.md)
