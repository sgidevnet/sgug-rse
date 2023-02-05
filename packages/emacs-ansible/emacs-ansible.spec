%global pkg ansible

Name:           emacs-%{pkg}
Version:        0.3.1
Release:        1%{?dist}
Summary:        Ansible minor mode

License:        GPLv3+
URL:            https://github.com/k1LoW/%{name}/
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{pkg}-init.el

BuildRequires:  emacs
BuildRequires:  emacs-f
BuildRequires:  emacs-s
Requires:       emacs(bin) >= %{_emacs_version}
Requires:       emacs-f
Requires:       emacs-s
BuildArch:      noarch

%description
%{summary}.


%prep
%autosetup


%build
%{_emacs_bytecompile} %{pkg}.el


%install
install -dm 0755 $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
install -pm 0644 %{pkg}.el* -t $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
cp -a dict/ snippets/ $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/

install -Dpm 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_emacs_sitestartdir}/%{pkg}-init.el


%files
%doc README.md
%license LICENSE
%{_emacs_sitelispdir}/%{pkg}/
%{_emacs_sitestartdir}/*.el


%changelog
* Tue Sep 01 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.3.1-1
- Update to 0.3.1

* Thu Aug 20 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.3.0-1
- Initial RPM release
