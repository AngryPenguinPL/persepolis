Name:           persepolis
Version:        3.1.0
Release:        1
Summary:        A powerful download manager powered by aria2
Group:          Networking/File transfer
License:        GPLv3+
URL:            https://persepolisdm.github.io/
Source0:        https://github.com/persepolisdm/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# Disable checking for runtime dependencies in setup.py.
Patch0:         persepolis-nodepscheck.diff

BuildArch:      noarch
BuildRequires:  pkgconfig(python)
BuildRequires:  python-qt5
BuildRequires:  desktop-file-utils
BuildRequires:  python3egg(setuptools)
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:  python3egg(requests)
BuildRequires:  python3egg(setproctitle)

# libnotify is required for notify-send
Requires:       aria2 
Requires:       libnotify 
Requires:       python-qt5 
Requires:       python-requests
Requires:       python-setproctitle
Requires:       sound-theme-freedesktop 
Requires:       python-psutil
Requires:       pulseaudio-utils 
# Package optional and from contrib repo. Make it recommends to pass test.
Recommends:     youtube-dl


%description
Persepolis is a download manager and a GUI for aria2 powered by Python.
 - Graphical UI front end for aria2
 - Multi-segment downloading
 - Scheduling downloads
 - Download queue
 
%prep
%autosetup -p1

%build
%{py_build}

%install
%{py_install}
chmod a+x %{buildroot}/%{python3_sitelib}/persepolis/__main__.py

%files
%license LICENSE
%doc README.md

%{_bindir}/%{name}
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/pixmaps/*
%{_mandir}/man1/%{name}.1*
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-%{version}-py?.?.egg-info
%{_datadir}/metainfo/com.github.persepolisdm.persepolis.appdata.xml
