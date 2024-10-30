



public class Main{
  public static void main(String[] args) {
    // args = new String[12];

    double health =  Math.round(6 *(Integer.parseInt(args[0]) * 0.2)) + 10;
    double agility =  Math.round(6 *(Integer.parseInt(args[1]) * 0.3)) + 10;
    double charisma =  Math.round(6 *(Integer.parseInt(args[2]) * 0.1)) + 10;
    double knowledge =  Math.round(6 *(Integer.parseInt(args[3]) * 0.05)) + 10;
    double energy =  Math.round(6 *(Integer.parseInt(args[4]) * 0.05)) + 10;
    double resourcefulness =  Math.round(6 *(Integer.parseInt(args[5]) * 0.3)) + 10;
    
    double health_weight = health * 0.18;
    double agility_weight = agility * 0.20;
    double charisma_weight = charisma * 0.21;
    double knowledge_weight = knowledge * 0.08;
    double energy_weight = energy * 0.17;
    double resourcefulness_weight  = resourcefulness * 0.16;
    long overall_value = Math.round(5 * (health_weight + agility_weight  + charisma_weight  + knowledge_weight + energy_weight + resourcefulness_weight));
    // args[0]="int";
    System.out.println(overall_value);
  }
  }
  