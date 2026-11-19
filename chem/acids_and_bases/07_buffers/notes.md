# 7. Buffers

AP topics **8.8 Properties of Buffers**, **8.9 Henderson–Hasselbalch Equation**, and **8.10 Buffer Capacity**

> **Goal:** Explain how a buffer resists pH change, calculate its pH, design a buffer for a target pH, and compare buffer capacities.

## What a buffer is

A buffer contains **large amounts of both members of a weak conjugate acid–base pair**:

| Buffer | Weak acid | Conjugate base |
|---|---|---|
| acetate | CH₃COOH | CH₃COO⁻ (from CH₃COONa) |
| ammonia | NH₄⁺ (from NH₄Cl) | NH₃ |
| phosphate | H₂PO₄⁻ | HPO₄²⁻ |
| blood (carbonic acid) | H₂CO₃ | HCO₃⁻ |

There are two ways to make one:
1. Mix a weak acid with a salt of its conjugate base, such as CH₃COOH + CH₃COONa.
2. Partly neutralize a weak acid with a strong base, or a weak base with a strong acid. Folder 3, Example 2 does this.

A strong acid and its salt (HCl + NaCl) is **not** a buffer, because Cl⁻ has no tendency to pick up H⁺.

## How a buffer works (8.8)

Each member of the pair neutralizes one kind of intruder:

```
Add strong acid:   CH₃COO⁻ + H₃O⁺ → CH₃COOH + H₂O      (the base member takes the H₃O⁺)
Add strong base:   CH₃COOH + OH⁻  → CH₃COO⁻ + H₂O      (the acid member takes the OH⁻)
```

The strong acid or base is converted into the **weak** member of the pair, so the [A⁻]/[HA] ratio changes only slightly, and so does the pH. You'll be asked for these net ionic equations often.

**Particle diagrams.** AP questions may show a beaker of particles. A buffer has *many* HA **and** *many* A⁻ particles. After acid is added, a few A⁻ have become HA. After base is added, a few HA have become A⁻.

## Henderson–Hasselbalch (8.9)

```
pH = pKa + log([A⁻] / [HA])
```

- It's on the formula sheet.
- You can use **moles** in place of concentrations, because both species are in the same volume.
- When [A⁻] = [HA], pH = pKa.
- **Choose a weak acid with pKa close to the target pH.** A buffer works well within about pKa ± 1.

**Example 1. Find the pH of a buffer containing 0.25 M CH₃COOH and 0.40 M CH₃COONa (pKa = 4.74).**

```
pH = 4.74 + log(0.40 / 0.25) = 4.74 + 0.20 = 4.95
```

There's more base than acid, so the pH is above pKa.

**Example 2. Design a buffer at pH 5.00 using acetic acid. What [CH₃COO⁻]/[CH₃COOH] ratio is needed?**

```
5.00 = 4.74 + log(ratio)    →    ratio = 10^(0.26) = 1.8
```

For example, use 0.18 M CH₃COONa with 0.10 M CH₃COOH.

**Example 3. Which acid would you use for a buffer at pH 7.4?**

| Choice | pKa |
|---|---|
| HCOOH | 3.74 |
| CH₃COOH | 4.74 |
| **H₂PO₄⁻** | **7.20** ← closest |
| NH₄⁺ | 9.26 |

Use H₂PO₄⁻ / HPO₄²⁻, a phosphate buffer.

### Diluting a buffer

Diluting a buffer with water **doesn't change its pH**, because the [A⁻]/[HA] ratio stays the same. It does reduce the buffer's **capacity**.

### What isn't tested

The AP exam **won't** ask you to calculate the change in pH when acid or base is added to an existing buffer, and won't ask you to derive Henderson–Hasselbalch. You still need to explain *qualitatively* which member reacts and why the pH barely moves. The partial-neutralization calculation (folder 3) is fair game. Your Advanced Chem 2 tests may include the addition calculation anyway, so the practice set has one marked **Beyond the AP exam**.

## Buffer capacity (8.10)

**Capacity** is how much strong acid or base a buffer can absorb before its pH changes a lot.

**1. More concentrated means more capacity, at the same pH.**

| Buffer | [HA] | [A⁻] | pH | Capacity |
|---|---|---|---|---|
| A | 0.10 M | 0.10 M | 4.74 | lower |
| B | 1.0 M | 1.0 M | 4.74 | **10 times higher** |

**2. The ratio decides which direction it handles better.**
- More A⁻ than HA: greater capacity for added **acid**, since there's more A⁻ to neutralize it.
- More HA than A⁻: greater capacity for added **base**.
- Equal amounts: balanced capacity in both directions.

**Real-world example: blood.** Blood is kept at pH 7.4 mainly by H₂CO₃/HCO₃⁻, with pKa ≈ 6.1 at body temperature.

```
[HCO₃⁻] / [H₂CO₃] = 10^(7.4 − 6.1) = 10^1.3 ≈ 20
```

There's about 20 times more base than acid, so blood is much better at neutralizing added **acid**. That's useful, because metabolism (exercise, for instance) produces acids such as lactic acid.

## Lab connection: experimental error (skill 6.G)

- **A buffer pH that's off from the H–H prediction** can come from mass or volume errors in preparing the components, or from a pH meter that wasn't calibrated.
- **A buffer that "fails" quickly** usually means its components were too dilute (low capacity) or it was used outside pKa ± 1.

## Common mistakes

- **Flipping the ratio.** It's base over acid: [A⁻]/[HA].
- **Using pKb instead of pKa for a base buffer.** For NH₃/NH₄⁺, use pKa of NH₄⁺ = 14.00 − pKb = 9.26.
- **Thinking a buffer keeps the pH constant.** It *resists* change. A small shift still happens, and a large addition overwhelms it.
- **Saying dilution changes buffer pH.** The ratio is unchanged, so the pH is too. Only the capacity drops.
- **Calling HCl + NaCl a buffer.** The pair must be a *weak* acid and its conjugate base.

➡️ Next: [practice.md](practice.md)
