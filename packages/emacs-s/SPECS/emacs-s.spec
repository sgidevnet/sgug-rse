%global pkg s

Name:           emacs-%{pkg}
Version:        1.12.0
Release:        1%{?dist}
Summary:        The long lost Emacs string manipulation library

License:        GPLv3+
URL:            https://github.com/magnars/%{pkg}.el/
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  emacs
Requires:       emacs(bin) >= %{_emacs_version}
BuildArch:      noarch

%description
%{summary}.


%prep
%autosetup -n %{pkg}.el-%{version}


%build
%{_emacs_bytecompile} %{pkg}.el


%install
install -dm 0755 $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
install -pm 0644 %{pkg}.el* -t $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/


%check
./run-tests.sh


%files
%doc README.md
%license LICENSE
%{_emacs_sitelispdir}/%{pkg}/


%changelog
* Thu Aug 20 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.12.0-1
- Initial RPM release
