#include <algorithm>
#include <array>
#include <cmath>
#include <iostream>
#include <limits>
#include <sstream>
#include <string>
#include <vector>

struct Position { int stringIndex, fret; };
struct Step { Position pos; int cost, parent; };

int main(int argc, char** argv) {
    const std::array<int, 6> open = {40, 45, 50, 55, 59, 64};
    if (argc < 2) { std::cerr << "Usage: fret-path MIDI_NOTE ...\n"; return 2; }
    std::vector<std::vector<Step>> layers;
    for (int i = 1; i < argc; ++i) {
        std::istringstream input(argv[i]);
        int note;
        if (!(input >> note) || !input.eof() || note < 40 || note > 84) {
            std::cerr << "Use whole MIDI notes from 40 to 84\n"; return 2;
        }
        std::vector<Step> options;
        for (int s = 0; s < 6; ++s) {
            int fret = note - open[s];
            if (fret < 0 || fret > 20) continue;
            Step step{{s, fret}, 0, -1};
            if (!layers.empty()) {
                step.cost = std::numeric_limits<int>::max();
                const auto& previous = layers.back();
                for (int j = 0; j < static_cast<int>(previous.size()); ++j) {
                    const auto& p = previous[j];
                    int cost = p.cost + std::abs(fret - p.pos.fret) + std::abs(s - p.pos.stringIndex);
                    if (cost < step.cost) { step.cost = cost; step.parent = j; }
                }
            }
            options.push_back(step);
        }
        layers.push_back(options);
    }
    const auto& last = layers.back();
    auto winner = std::min_element(last.begin(), last.end(), [](auto a, auto b){ return a.cost < b.cost; });
    std::cout << "Movement score: " << winner->cost << '\n';
    int index = static_cast<int>(winner - last.begin());
    std::vector<Position> path;
    for (auto it = layers.rbegin(); it != layers.rend(); ++it) {
        const auto& step = (*it)[index];
        path.push_back(step.pos);
        index = step.parent;
    }
    for (auto it = path.rbegin(); it != path.rend(); ++it)
        std::cout << "String " << 6 - it->stringIndex << ", fret " << it->fret << '\n';
}
