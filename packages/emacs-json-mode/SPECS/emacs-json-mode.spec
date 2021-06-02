%global pkg json-mode

Name:           emacs-%{pkg}
Version:        1.7.0
Release:        3%{?dist}
Summary:        Major mode for editing JSON files with Emacs

License:        GPLv3+
URL:            https://github.com/joshwnj/%{pkg}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{pkg}-init.el

BuildRequires:  emacs
BuildRequires:  emacs-json-reformat
BuildRequires:  emacs-json-snatcher
Requires:       emacs(bin) >= %{_emacs_version}
Requires:       emacs-json-reformat
Requires:       emacs-json-snatcher
BuildArch:      noarch

%description
Major mode for editing JSON files.

Extends the builtin js-mode to add better syntax highlighting for JSON.


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
%{_emacs_sitelispdir}/%{pkg}/
%{_emacs_sitestartdir}/*.el


%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 22 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.7.0-1
- Initial RPM release
