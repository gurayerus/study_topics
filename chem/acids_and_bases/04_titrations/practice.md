# Practice: Titrations

Assume 25 °C. Try each problem before opening the solution.

---

**1.** A student standardizes a NaOH solution by titrating 0.5105 g of potassium hydrogen phthalate (KHP, KHC₈H₄O₄, molar mass 204.22 g/mol), a monoprotic acid. The endpoint is reached after 22.45 mL of NaOH. What is the molarity of the NaOH?

<details><summary>Show solution</summary>

```
mol KHP  = 0.5105 g / 204.22 g/mol = 2.500 × 10⁻³ mol
mol NaOH = mol KHP (1:1 at equivalence)
[NaOH]   = 2.500 × 10⁻³ mol / 0.02245 L = 0.1113 M
```

</details>

---

**2. (Full titration)** 20.00 mL of 0.150 M propanoic acid, CH₃CH₂COOH (Ka = 1.3 × 10⁻⁵), is titrated with 0.100 M NaOH.

(a) What volume of NaOH is needed to reach the equivalence point?
(b) Calculate the pH before any NaOH is added.
(c) Calculate the pH after 10.00 mL of NaOH is added.
(d) Calculate the pH after 15.00 mL of NaOH is added.
(e) Calculate the pH at the equivalence point.
(f) Calculate the pH after 35.00 mL of NaOH is added.
(g) Which indicator is best for this titration: methyl red (pKa ≈ 5.0), bromothymol blue (pKa ≈ 7.1), or phenolphthalein (pKa ≈ 9.4)? Justify your answer.

<details><summary>Show solution</summary>

pKa = −log(1.3 × 10⁻⁵) = 4.89. There are 20.00 × 0.150 = 3.00 mmol of acid.

(a) V = 3.00 mmol / 0.100 M = **30.00 mL**

(b) Weak acid only:
```
[H₃O⁺] = √(1.3 × 10⁻⁵ × 0.150) = 1.40 × 10⁻³ M        pH = 2.86
```

(c) 1.00 mmol OH⁻ added:
```
HA: 3.00 − 1.00 = 2.00 mmol     A⁻: 1.00 mmol
pH = 4.89 + log(1.00/2.00) = 4.89 − 0.30 = 4.59
```

(d) 15.00 mL is **half** of 30.00 mL, so this is the half-equivalence point: **pH = pKa = 4.89**.

(e) All 3.00 mmol is now A⁻, in 50.00 mL:
```
[A⁻]  = 3.00 / 50.00 = 0.0600 M
Kb    = 1.0 × 10⁻¹⁴ / 1.3 × 10⁻⁵ = 7.7 × 10⁻¹⁰
[OH⁻] = √(7.7 × 10⁻¹⁰ × 0.0600) = 6.8 × 10⁻⁶ M
pOH = 5.17        pH = 8.83
```

(f) 3.50 mmol OH⁻ added and 3.00 mmol used, leaving 0.50 mmol excess in 55.00 mL:
```
[OH⁻] = 0.50 / 55.00 = 9.1 × 10⁻³ M     pOH = 2.04     pH = 11.96
```

(g) **Phenolphthalein.** Its pKa (about 9.4) is closest to the pH at the equivalence point (8.83), so it changes color in the steep part of the curve, right at equivalence. Methyl red would change color around pH 5, in the buffer region, long before equivalence.

</details>

---

**3. (Reading a curve)** 20.00 mL of an unknown weak monoprotic acid is titrated with 0.120 M NaOH. From the titration curve, the equivalence point is at 24.0 mL, and the pH at 12.0 mL is 3.75.

(a) Calculate the initial concentration of the acid.
(b) Calculate Ka.
(c) Use the table to identify the acid.

| Acid | Ka |
|---|---|
| HF | 6.8 × 10⁻⁴ |
| HCOOH | 1.8 × 10⁻⁴ |
| CH₃COOH | 1.8 × 10⁻⁵ |

<details><summary>Show solution</summary>

(a)
```
mol NaOH = 0.0240 L × 0.120 M = 2.88 × 10⁻³ mol = mol HA
[HA]     = 2.88 × 10⁻³ / 0.02000 L = 0.144 M
```

(b) 12.0 mL is half of 24.0 mL, so pH = pKa = 3.75.
```
Ka = 10^(−3.75) = 1.8 × 10⁻⁴
```

(c) **Formic acid, HCOOH.**

</details>

---

**4.** Equal volumes of 0.10 M HCl and 0.10 M CH₃COOH are titrated separately with 0.10 M NaOH. Which statement is correct?

(A) The CH₃COOH requires less NaOH to reach equivalence because it is a weak acid.
(B) The two titrations require the same volume of NaOH, and both have a pH of 7.00 at equivalence.
(C) The two titrations require the same volume of NaOH, but the pH at equivalence is higher for CH₃COOH.
(D) The HCl requires more NaOH because it produces more H₃O⁺ ions.

<details><summary>Show solution</summary>

**(C).** The moles of acid are equal, so the equivalence volumes are equal. At equivalence, the CH₃COOH flask contains CH₃COO⁻, a weak base, so its pH is above 7. The HCl flask contains only Na⁺ and Cl⁻, so its pH is 7.00.

</details>

---

**5. (Polyprotic, qualitative)** 20.00 mL of a diprotic acid H₂A is titrated with 0.100 M NaOH. The titration curve has two vertical jumps, at 15.0 mL and 30.0 mL. The pH is 4.20 at 7.5 mL and 7.00 at 22.5 mL.

(a) How does the curve show that H₂A is diprotic?
(b) Calculate the initial concentration of H₂A.
(c) Estimate pKa₁ and pKa₂.
(d) Identify the major A-containing species present at 15.0 mL, at 22.5 mL, and at 35.0 mL.

<details><summary>Show solution</summary>

(a) There are **two** equivalence points (two vertical jumps), one for each acidic proton.

(b) The first equivalence point removes one proton from every H₂A:
```
mol H₂A = 0.0150 L × 0.100 M = 1.50 × 10⁻³ mol
[H₂A]   = 1.50 × 10⁻³ / 0.02000 L = 0.0750 M
```

(c) 7.5 mL is half of the first equivalence volume, so **pKa₁ ≈ 4.20**. 22.5 mL is halfway between the two equivalence points, so **pKa₂ ≈ 7.00**.

(d)
- 15.0 mL (first equivalence): **HA⁻**
- 22.5 mL (second half-equivalence): **HA⁻ and A²⁻ in equal amounts**
- 35.0 mL (past the second equivalence): **A²⁻**, along with excess OH⁻

Calculating the concentration of each species at these points is **not** on the AP exam, but this kind of reasoning is.

</details>

---

**6. (Lab error analysis)** A student titrates 25.00 mL of acetic acid with standardized NaOH to find the acid's concentration. For each error, state whether the calculated concentration of the acetic acid would be too high, too low, or unaffected. Justify each answer.

(a) The student rinsed the buret with distilled water but not with the NaOH solution before filling it.
(b) The student added 20 mL of distilled water to the flask of acetic acid before titrating.
(c) There was an air bubble in the buret tip at the start, and it disappeared during the titration.

<details><summary>Show solution</summary>

The calculated [acid] = (M_NaOH × V_NaOH) / 25.00 mL, using the *labeled* M_NaOH.

(a) **Too high.** Leftover water dilutes the NaOH, so more volume is needed to deliver the required moles of OH⁻. The larger V_NaOH, multiplied by the labeled (too high) molarity, overstates the moles of acid.

(b) **No effect.** Adding water doesn't change the moles of acetic acid in the flask, so the same moles of NaOH, and the same volume, are needed to reach equivalence.

(c) **Too high.** Part of the recorded volume change was the bubble filling with liquid, not NaOH entering the flask. The recorded V_NaOH is larger than the volume actually delivered.

</details>

---

**7.** In a titration of NH₃(aq) with HCl(aq), which is true at the equivalence point?

(A) pH = 7.00, because the acid and base have exactly neutralized each other.
(B) pH > 7, because excess NH₃ remains.
(C) pH < 7, because NH₄⁺ reacts with water to produce H₃O⁺.
(D) pH = pKa of NH₄⁺.

<details><summary>Show solution</summary>

**(C).** At equivalence, all the NH₃ has become NH₄⁺, a weak acid: NH₄⁺ + H₂O ⇌ NH₃ + H₃O⁺. Choice (D) describes the *half*-equivalence point.

</details>

➡️ Next topic: [5. Structure and acid strength](../05_structure_and_acid_strength/notes.md)
