%global pkg f

Name:           emacs-%{pkg}
Version:        0.20.0
Release:        1%{?dist}
Summary:        Modern API for working with files and directories in Emacs

License:        GPLv3+
URL:            https://github.com/rejeep/%{pkg}.el/
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  emacs
BuildRequires:  emacs-dash
BuildRequires:  emacs-s
Requires:       emacs(bin) >= %{_emacs_version}
Requires:       emacs-dash
Requires:       emacs-s
BuildArch:      noarch

%description
f.el is a modern API for working with files and directories in Emacs.


%prep
%autosetup -n %{pkg}.el-%{version}


%build
%{_emacs_bytecompile} %{pkg}.el


%install
install -dm 0755 $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
install -pm 0644 %{pkg}.el* -t $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/


%files
%doc CHANGELOG.md README.md
%{_emacs_sitelispdir}/%{pkg}/


%changelog
* Thu Aug 20 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.20.0-1
- Initial RPM release
