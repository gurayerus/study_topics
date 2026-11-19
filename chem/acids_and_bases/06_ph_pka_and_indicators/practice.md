# Practice: pH, pKa, and indicators

Assume 25 °C. Try each problem before opening the solution.

---

**1.** Acetic acid has pKa = 4.74. For solutions at each pH below, state which form (CH₃COOH or CH₃COO⁻) is present in greater concentration, and estimate the ratio.

(a) pH 3.00  (b) pH 4.74  (c) pH 6.00

<details><summary>Show solution</summary>

(a) pH < pKa, so **CH₃COOH** dominates. [CH₃COOH]/[CH₃COO⁻] = 10^(4.74 − 3.00) = 10^1.74 ≈ **55**.

(b) pH = pKa, so the two forms are **equal**: [CH₃COOH] = [CH₃COO⁻].

(c) pH > pKa, so **CH₃COO⁻** dominates. [CH₃COO⁻]/[CH₃COOH] = 10^(6.00 − 4.74) = 10^1.26 ≈ **18**.

</details>

---

**2.** A weak acid HA has pKa = 6.0. In a solution buffered at pH 8.0, what is the ratio [A⁻]/[HA]?

(A) 0.01  (B) 2  (C) 100  (D) 1.3

<details><summary>Show solution</summary>

**(C).** [A⁻]/[HA] = 10^(8.0 − 6.0) = 10² = 100. Choice (D), 8.0/6.0, comes from treating pH as linear.

</details>

---

**3.** Bromocresol green is an indicator with pKa ≈ 4.7. Its HIn form is yellow and its In⁻ form is blue. What color is it in a solution at (a) pH 3.0, (b) pH 4.7, and (c) pH 7.0?

<details><summary>Show solution</summary>

(a) pH < pKa, so HIn dominates: **yellow**.
(b) pH = pKa, so equal amounts of yellow and blue: **green**. That's where its name comes from.
(c) pH > pKa, so In⁻ dominates: **blue**.

</details>

---

**4.** NH₃ is titrated with HCl, and the pH at the equivalence point is 5.28. Which indicator is the best choice? Justify your answer.

| Indicator | pKa |
|---|---|
| methyl orange | 3.5 |
| methyl red | 5.0 |
| bromothymol blue | 7.1 |
| phenolphthalein | 9.4 |

<details><summary>Show solution</summary>

**Methyl red.** Its pKa (5.0) is the closest to the equivalence-point pH (5.28), so its color changes on the steep part of the curve, right at equivalence. The endpoint will then match the equivalence point.

</details>

---

**5.** Phosphoric acid has pKa₁ = 2.15, pKa₂ = 7.20, and pKa₃ = 12.35. Identify the dominant phosphate species at each pH:

(a) pH 1.0 (b) pH 5.0 (c) pH 7.20 (d) pH 10.0 (e) pH 13.0

<details><summary>Show solution</summary>

(a) **H₃PO₄**, since pH < pKa₁.
(b) **H₂PO₄⁻**, since pH is between pKa₁ and pKa₂.
(c) **H₂PO₄⁻ and HPO₄²⁻ in equal amounts**, since pH = pKa₂.
(d) **HPO₄²⁻**, since pH is between pKa₂ and pKa₃.
(e) **PO₄³⁻**, since pH > pKa₃.

</details>

---

**6.** A student prepares a solution containing equal concentrations of a weak acid HA and its sodium salt NaA. The pH meter reads 4.20. Calculate Ka for HA.

<details><summary>Show solution</summary>

When [HA] = [A⁻], pH = pKa, so pKa = 4.20.

```
Ka = 10^(−4.20) = 6.3 × 10⁻⁵
```

This matches benzoic acid.

</details>

---

**7. (Free-response style)** A student titrates 25.00 mL of NH₃(aq) with standardized HCl but uses **phenolphthalein** (pKa ≈ 9.4, pink above about pH 8.2, colorless below) as the indicator. The equivalence-point pH for this titration is 5.28.

(a) At the start of the titration, what color is the solution? Explain.

(b) Will the endpoint (the color change) occur before, at, or after the equivalence point? Explain.

(c) How will this error affect the calculated concentration of NH₃: too high, too low, or no effect? Justify your answer.

<details><summary>Show solution</summary>

(a) **Pink.** The NH₃ solution is basic (pH about 11), well above phenolphthalein's pKa, so the In⁻ (pink) form dominates.

(b) **Before.** The pink color disappears as the pH drops through about 9 to 8.2. That happens in the buffer region (pKa of NH₄⁺ = 9.26), when only about 90% of the NH₃ has reacted, well before the equivalence point at pH 5.28.

(c) **Too low.** The student stops adding HCl too early, so the recorded volume of HCl is smaller than the true equivalence volume. Fewer moles of HCl are recorded, so fewer moles of NH₃ are calculated, and the calculated concentration is too low.

</details>

➡️ Next topic: [7. Buffers](../07_buffers/notes.md)
