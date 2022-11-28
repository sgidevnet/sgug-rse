%global pkg rpm-spec-mode
%global git_hash 7d06d19a31e888b932da6c8202ff2c73f42703a1

Name:           emacs-%{pkg}
Version:        0.16
Release:        7%{?dist}
Summary:        Major GNU Emacs mode for editing RPM spec files

License:        GPLv2+
URL:            https://github.com/bjorlykke/rpm-spec-mode/
Source0:        https://raw.githubusercontent.com/bjorlykke/rpm-spec-mode/%{git_hash}/rpm-spec-mode.el
Source1:        rpm-spec-mode-init.el

BuildArch:      noarch
BuildRequires:  emacs
Requires:       emacs(bin) >= %{_emacs_version}

%description
Major GNU Emacs mode for editing RPM spec files.

%prep
%setup -q -n rpm-spec-mode-%{version} -T -c
cp %SOURCE0 $RPM_BUILD_DIR/rpm-spec-mode-%{version}

%build
%_emacs_bytecompile rpm-spec-mode.el

%install
mkdir -p %{buildroot}/%{_emacs_sitelispdir}/rpm-spec-mode
install -m 644 rpm-spec-mode.el{,c} %{buildroot}/%{_emacs_sitelispdir}/rpm-spec-mode

# Install rpm-spec-mode-init.el
mkdir -p %{buildroot}%{_emacs_sitestartdir}
install -m 644 %SOURCE1 %{buildroot}%{_emacs_sitestartdir}

%files
%{_emacs_sitestartdir}/rpm-spec-mode-init.el
%{_emacs_sitelispdir}/rpm-spec-mode/rpm-spec-mode.el
%{_emacs_sitelispdir}/rpm-spec-mode/rpm-spec-mode.elc

%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jun  7 2016 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.16-1
- Update to 0.16

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 16 2014 Michel Salim <salimma@fedoraproject.org> - 0.15-1
- Update to 0.15

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 14 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 0.12-5
- Fix and apply patch for rpm-goto-add-change-log-entry (#970924)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Sep 19 2012 Karel Klíč <kklic@redhat.com> - 0.12-3
- Removed build dependency on emacs-el
- Require emacs without embedded rpm-spec-mode to avoid conflicts
  during updates

* Tue Sep 18 2012 Karel Klíč <kklic@redhat.com> - 0.12-2
- Moved rpm-spec-mode.el{,c} to a subdirectory

* Fri Sep 14 2012 Karel Klíč <kklic@redhat.com> - 0.12-1
- Initial package
