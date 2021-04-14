Name:           cowsay-beefymiracle
Version:        1.0
Release:        13%{?dist}
Summary:        Cowsay file for the Beefy Miracle

License:        CC-BY-SA
URL:            http://rrix.fedorapeople.org/beefsay
Source0:        http://rrix.fedorapeople.org/beefsay/beefymiracle.cow

BuildRequires:  cowsay
Requires:       cowsay

BuildArch:      noarch

%description
Provides a cowsay file for His Holiness the Beefy Miracle. It can be invoked
using cowsay -f beefymiracle, or aliased appropriately.

%prep
# Nothing to do

%build
# Nothing to do


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_datadir}/cowsay/
install %SOURCE0 %{buildroot}/%{_datadir}/cowsay/beefymiracle.cow
sed -i -e 's,/bin/env perl,/usr/sgug/bin/env perl,g' %{buildroot}/%{_datadir}/cowsay/beefymiracle.cow


%check
export COWPATH=%{buildroot}%{_datadir}/cowsay
echo Installation successful | cowsay -f beefymiracle


%files
%doc
%{_datadir}/cowsay/beefymiracle.cow

%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 30 2018 Adam Williamson <awilliam@redhat.com> - 1.0-11
- Hack shebang to not use env, to avoid broken /bin/perl dependency

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Ryan Rix <ry@n.rix.si> - 1.0-1
- Initial packaging of cowsay plugin
