Name:           zsh-lovers
Version:        0.9.1
Release:        2%{?dist}
Summary:        A collection of tips, tricks and examples for the Z shell
License:        GPLv2
URL:            https://grml.org/zsh/#zshlovers
Source0:        https://deb.grml.org/pool/main/z/zsh-lovers/zsh-lovers_%{version}.tar.xz
BuildArch:      noarch
BuildRequires:  asciidoc

%description
zsh-lovers is a small project which tries to collect tips, tricks and examples
for the Z shell. 

This package only ships a manpage of the collection.

%prep
%autosetup

%build
a2x -vv -L -f manpage zsh-lovers.1.txt

%install
install -pDm644 zsh-lovers.1 %{buildroot}%{_mandir}/man1/zsh-lovers.1

%files
%doc README.md
%license COPYING
%{_mandir}/man1/zsh-lovers.1*

%changelog
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 21 2019 Filipe Rosset <rosset.filipe@gmail.com> - 0.9.1-1
- Update to 0.9.1 fixes rhbz#1417333

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr 21 2014 Christopher Meng <rpm@cicku.me> - 0.9.0-1
- Initial Package.
