Summary:	Game like Nibbles but different
Summary(pl):	Gra w stylu Nibbles, ale inna
Name:		heroes
Version:	0.12
Release:	5
License:	GPL
Group:		Applications/Games
Source0:	http://dl.sourceforge.net/heroes/%{name}-%{version}.tar.bz2
Source1:	http://dl.sourceforge.net/heroes/%{name}-data-1.1.tar.bz2
Source2:	http://dl.sourceforge.net/heroes/%{name}-sound-tracks-1.0.tar.bz2
Source3:	http://dl.sourceforge.net/heroes/%{name}-sound-effects-1.0.tar.bz2
URL:		http://heroes.sourceforge.net/
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	bison
BuildRequires:	gettext
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Heroes is similar to the "Tron" and "Nibbles" games of yore, but
includes many graphical improvements and new game features. In it, you
must maneuver a small vehicle around a world and collect powerups
while avoiding obstacles, your opponents' trails, and even your own
trail. Several modes of play are available, including
"get-all-the-bonuses", deathmatch, and "squish-the-pedestrians".

%description -l pl
Heroes jest podobny do starych gier "Tron" i "Nibbles", ale zawiera
wiele graficznych ulepsze� i nowe w�asno�ci. W tej grze musisz
manewrowa� ma�ym pojazdem i zbiera� dopalacze, unikaj�c przeszk�d i
�lad�w przeciwnik�w, a nawet swojego w�asnego �ladu. S� dost�pne r�ne
tryby gry, w tym "zbierz-wszystkie-premie", deathmatch oraz
"rozjed�-pieszych".

%prep
%setup -q -a1 -a2 -a3

%build
%configure
%{__make}

cd %{name}-data-1.1
%configure
%{__make}
cd ..

for i in sound-effects sound-tracks; do
cd %{name}-$i-1.0
%configure
%{__make}
cd ..
done

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
cd %{name}-data-1.1
%makeinstall
cd ..
for i in sound-effects sound-tracks; do
cd %{name}-$i-1.0
%makeinstall
cd ..
done

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog NEWS README THANKS TODO
%{_datadir}/%{name}
%{_mandir}/*/*
%attr(755,root,root) %{_bindir}/*
