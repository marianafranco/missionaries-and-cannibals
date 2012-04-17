import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Set;

// based on the breadth-first search algorithm present on the 3o Edition of the
// "Artificial Intelligence A Modern Approach".
public class BreadthFirstSearch {

	public State exec(State initialState) {
		if (initialState.isGoal()) {
			return initialState;
		}
		Queue<State> frontier = new LinkedList<State>();	// FIFO queue
		Set<State> explored = new HashSet<State>();
		frontier.add(initialState);
		while (true) {
			if (frontier.isEmpty()) {
				return null;	// failure
			}
			State state = frontier.poll();
			explored.add(state);
			List<State> successors = state.generateSuccessors();
			for (State child : successors) {
				if (!explored.contains(child) || !frontier.contains(child)) {
					if (child.isGoal()) {
						return child;
					}
					frontier.add(child);
				}
			}
		}
	}
}
