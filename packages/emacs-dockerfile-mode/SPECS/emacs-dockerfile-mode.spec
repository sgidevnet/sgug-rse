%global pkg dockerfile-mode

Name:           emacs-%{pkg}
Version:        1.2
Release:        1%{?dist}
Summary:        An emacs mode for handling Dockerfiles

License:        ASL 2.0
URL:            https://github.com/spotify/%{pkg}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{pkg}-init.el

BuildRequires:  emacs
Requires:       emacs(bin) >= %{_emacs_version}
BuildArch:      noarch

%description
This package provides a major mode `dockerfile-mode' for use with the standard
`Dockerfile' file format.  Additional convenience functions allow images to be
built easily.


%prep
%autosetup -n %{pkg}-%{version}


%build
%{_emacs_bytecompile} %{pkg}.el


%install
install -dm 0755 $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
install -pm 0644 %{pkg}.el* -t $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/

install -Dpm 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_emacs_sitestartdir}/%{pkg}-init.el


%files
%doc README.md
%license LICENSE
%{_emacs_sitelispdir}/%{pkg}/
%{_emacs_sitestartdir}/*.el


%changelog
* Tue Sep 03 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.2-1
- Initial RPM release
