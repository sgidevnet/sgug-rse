%global game_name berusky2

Summary:        A datafile for Berusky
Name:           berusky2-data
Version:        0.12
Release:        1%{?dist}
License:        GPLv2+
Source:         http://downloads.sourceforge.net/%{game_name}/%{name}-%{version}.tar.xz
URL:            http://www.anakreon.cz/en/Berusky2.htm
BuildArch:      noarch

%description
This package contains the game data for %{game_name}, i.e. files with graphics,
levels, game rules and configuration.

%prep
%setup -q

%install
mkdir -p %{buildroot}%{_datadir}/%{game_name}

mv bitmap \
   data \
   game \
   game_data \
   items \
   materials \
   out \
   textures \
   music \
   sound \
   %{buildroot}%{_datadir}/%{game_name}

%files
%{_datadir}/%{game_name}

%changelog
* Tue Jun 30 2020 Martin Stransky <stransky@redhat.com> - 0.12-1
- new upstream tarball (0.12)

* Fri Jun 19 2020 Martin Stransky <stransky@redhat.com> - 0.10-1
- new upstream tarball (0.10)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Mar 31 2013 Martin Stransky <stransky@redhat.com> 0.9-1
- new upstream tarball (0.9)

* Sun Feb 24 2013 Martin Stransky <stransky@redhat.com> 0.7-1
- new upstream tarball (0.7)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May  7 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.6-2
- Bump build

* Sun Mar 4 2012 Martin Stransky <stransky@redhat.com> 0.6-1
- new upstream tarball

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Aug 30 2011 Martin Stransky <stransky@redhat.com> 0.5-1
- new upstream tarball
- spec clean up (by Richard Shaw)

* Sat Aug 20 2011 Martin Stransky <stransky@redhat.com> 0.4-1
- ini file and save/profile dir were moved to binary package

* Mon Aug 15 2011 Martin Stransky <stransky@redhat.com> 0.3-1
- initial build
