# 3. Acid–base reactions and mixtures

AP topic **8.4 Acid–Base Reactions and Buffers**

> **Goal:** Given any mixture of an acid and a base, figure out what's left after they react and calculate the pH.

## The rule: react first, then equilibrate

Whenever a **strong** acid or base is involved, the reaction goes to completion. Every problem has two steps:

1. **Stoichiometry (work in moles).** Let the strong species react completely with whatever it can. Find out what's left.
2. **Equilibrium.** Look at what's left and choose the right method for the pH.

Work in **moles** (or millimoles: mL × M = mmol) for the stoichiometry, since the volumes change when solutions are mixed. Convert back to molarity using the **total** volume.

## Net ionic equations

Write strong acids and bases as ions, write weak ones as molecules, and drop the spectator ions.

| Mixture | Net ionic equation | Goes to |
|---|---|---|
| strong acid + strong base | H₃O⁺ + OH⁻ → 2 H₂O | completion |
| weak acid + strong base | HA + OH⁻ → A⁻ + H₂O | completion |
| weak base + strong acid | B + H₃O⁺ → HB⁺ + H₂O | completion |
| weak acid + weak base | HA + B ⇌ A⁻ + HB⁺ | equilibrium |

Examples: CH₃COOH + OH⁻ → CH₃COO⁻ + H₂O and NH₃ + H₃O⁺ → NH₄⁺ + H₂O.

Free-response questions ask for these often. Writing CH₃COOH as H⁺ + CH₃COO⁻ loses the point, because acetic acid is mostly un-ionized.

## The decision map

After the stoichiometry step, here's what's left and how to get the pH:

| What's left after reaction | It's a… | pH method |
|---|---|---|
| excess strong acid | strong acid solution | [H₃O⁺] = excess mol / total V |
| excess strong base | strong base solution | [OH⁻] = excess mol / total V |
| strong + strong, exactly equal | neutral salt | pH = 7.00 |
| weak acid **and** its conjugate base | **buffer** | Henderson–Hasselbalch (folder 7) |
| only the conjugate base A⁻ (equal moles of weak acid and strong base) | weak base | Kb = Kw/Ka, then ICE → **pH > 7** |
| only the conjugate acid HB⁺ (equal moles of weak base and strong acid) | weak acid | Ka = Kw/Kb, then ICE → **pH < 7** |

The Henderson–Hasselbalch equation is pH = pKa + log(mol A⁻ / mol HA). You can use moles directly because both species are in the same volume. Folder 7 covers it in detail.

## Worked examples

All use CH₃COOH with Ka = 1.8 × 10⁻⁵ (pKa = 4.74).

**Example 1 (strong + strong). Mix 25.0 mL of 0.100 M HCl with 15.0 mL of 0.100 M NaOH.**

```
mmol H₃O⁺ = 25.0 × 0.100 = 2.50        mmol OH⁻ = 15.0 × 0.100 = 1.50
                H₃O⁺  +  OH⁻  →  2 H₂O
Before          2.50     1.50
After           1.00     0
[H₃O⁺] = 1.00 mmol / 40.0 mL = 0.0250 M        pH = 1.60
```

**Example 2 (weak acid in excess, so a buffer forms). Mix 50.0 mL of 0.10 M CH₃COOH with 20.0 mL of 0.10 M NaOH.**

```
mmol CH₃COOH = 5.0        mmol OH⁻ = 2.0
              CH₃COOH  +  OH⁻  →  CH₃COO⁻  +  H₂O
Before          5.0       2.0        0
After           3.0       0          2.0
```

Both members of the conjugate pair are present, so this is a buffer:

```
pH = pKa + log(2.0 / 3.0) = 4.74 + (−0.18) = 4.57
```

**Example 3 (equal moles, so only the conjugate base remains). Mix 50.0 mL of 0.10 M CH₃COOH with 50.0 mL of 0.10 M NaOH.**

```
              CH₃COOH  +  OH⁻  →  CH₃COO⁻  +  H₂O
Before          5.0       5.0        0
After           0         0          5.0
[CH₃COO⁻] = 5.0 mmol / 100.0 mL = 0.050 M
```

What's left is a weak base:

```
CH₃COO⁻ + H₂O ⇌ CH₃COOH + OH⁻
Kb    = 1.0 × 10⁻¹⁴ / 1.8 × 10⁻⁵ = 5.6 × 10⁻¹⁰
[OH⁻] = √(5.6 × 10⁻¹⁰ × 0.050) = 5.3 × 10⁻⁶ M
pOH = 5.28        pH = 8.72
```

"Neutralized" does **not** mean pH 7 when a weak acid or base is involved.

**Example 4 (strong base in excess). Mix 50.0 mL of 0.10 M CH₃COOH with 60.0 mL of 0.10 M NaOH.**

```
After reaction: 0 CH₃COOH, 5.0 mmol CH₃COO⁻, 1.0 mmol OH⁻ left over
[OH⁻] = 1.0 mmol / 110.0 mL = 9.1 × 10⁻³ M        pOH = 2.04        pH = 11.96
```

The leftover OH⁻ is the only thing that matters. The OH⁻ made by CH₃COO⁻ is negligible next to it.

## Weak acid + weak base

Neither species is strong, so the reaction reaches an equilibrium instead of going to completion:

```
HA + B ⇌ A⁻ + HB⁺          K = Ka(HA) × Kb(B) / Kw = Ka(HA) / Ka(HB⁺)
```

**Read it as:** the reaction favors products if the acid on the left (HA) is stronger than the acid on the right (HB⁺).

| Reaction | K | Favors |
|---|---|---|
| HF + NH₃ ⇌ F⁻ + NH₄⁺ | (6.8 × 10⁻⁴)(1.8 × 10⁻⁵) / 10⁻¹⁴ = 1.2 × 10⁶ | products |
| CH₃COOH + NH₃ ⇌ CH₃COO⁻ + NH₄⁺ | 3.2 × 10⁴ | products |
| HCN + NH₃ ⇌ CN⁻ + NH₄⁺ | 1.1 | neither strongly |

## Common mistakes

- **Using concentrations instead of moles in the stoichiometry step.** Mixing changes the volume, so moles are the safe unit.
- **Forgetting the total volume** when converting excess moles back to molarity.
- **Assuming pH 7 after "neutralization"** of a weak acid or base.
- **Doing an ICE table before the strong reaction.** A strong acid or base reacts completely first, before any equilibrium calculation.
- **Writing weak acids as ions** in net ionic equations.

➡️ Next: [practice.md](practice.md)
