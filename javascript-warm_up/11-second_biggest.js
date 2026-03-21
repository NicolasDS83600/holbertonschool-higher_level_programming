#!/usr/bin/node
const args = process.argv.slice(2).map(Number);

if (args.length <= 1) {
  console.log(0);
} else {
  const biggest = Math.max(...args);
  const filtered = args.filter((n) => n !== biggest);
  console.log(filtered.length === 0 ? 0 : Math.max(...filtered));
}
