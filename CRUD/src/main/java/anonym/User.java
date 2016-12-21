package anonym;
/**
 * Autor: Kanyildiz Muhammedhizir
 * Klasse: 4AHITM
 * Datum: 06.10.2016
*/

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(name = "user")
public class User {
	@Id
	@Column(name = "id")
	private int id;
	@Column(name = "vorname")
	private String vorname;
	@Column(name = "nachname")
	private String nachname;
	@Column(name = "age")
	private Integer age;
	
	
	public User(int id, String vorname, String nachname, Integer age) {
		this.id = id;
		this.vorname = vorname;
		this.nachname = nachname;
		this.age = age;
	}
	public User() {
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getVorname() {
		return vorname;
	}

	public void setVorname(String vorname) {
		this.vorname = vorname;
	}

	public String getNachname() {
		return nachname;
	}

	public void setNachname(String nachname) {
		this.nachname = nachname;
	}

	public Integer getAge() {
		return age;
	}

	public void setAge(Integer age) {
		this.age = age;
	}

	
}