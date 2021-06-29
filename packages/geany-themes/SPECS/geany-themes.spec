Name:           geany-themes
Version:        1.27
Release:        7%{?dist}
Summary:        A collection of syntax highlighting color schemes for Geany

# Some of the color schemes are clearly stated as GPLv2+, some are BSD
License:        GPLv2+ and BSD

URL:            https://github.com/geany/geany-themes
Source0:        https://github.com/geany/geany-themes/releases/download/%{version}/geany-themes-%{version}.tar.bz2

Requires:       geany >= 1.24
BuildArch:      noarch


%description
Geany-Themes is a set of syntax highlighting color schemes for the Geany IDE.
Simply install this package, restart Geany and find the themes in
View->Editor->Color Schemes.


%prep
%setup -q


%build
# Nothing to build here. We just have to place some configuraton files into the
# proper directory..


%install
install -d $RPM_BUILD_ROOT%{_datadir}/geany/colorschemes
install -pm 644 colorschemes/*.conf $RPM_BUILD_ROOT%{_datadir}/geany/colorschemes


%files
%doc AUTHORS COPYING README.md
%{_datadir}/geany/colorschemes/*.conf


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.27-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.27-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.27-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Mar 30 2016 Oliver Haessler <oliver@redhat.com> - 1.27-1
- New upstream release: 1.27
- added new themes: darcula.conf, dark-colors.conf, himbeere.conf, sleepy-pastel.conf

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Apr 26 2014 Dominic Hopf <dmaphy@fedoraproject.org> - 1.24-1
- New upstream release: 1.24

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 28 2013 Dominic Hopf <dmaphy@fedoraproject.org> - 1.22.2-3
- update project URL

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 22 2012 Dominic Hopf <dmaphy@fedoraproject.org> - 1.22.2-1
- New upstream release: 1.22.2

* Tue Aug 14 2012 Dominic Hopf <dmaphy@fedoraproject.org> - 1.22-1
- initial package for Fedora
