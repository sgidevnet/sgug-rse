Name:           smem
Version:        1.5
Release:        3%{?dist}
Summary:        Report application memory usage in a meaningful way

License:        GPLv2+
URL:            http://www.selenic.com/smem/
# version 1.5 created from tag 1.5 at
# https://selenic.com/repo/smem/rev/1.5
Source0:        http://www.selenic.com/smem/download/smem-%{version}.tar.xz
BuildArch:      noarch

Patch0: 	smem-1.5-python3path.patch

%description
smem is a tool that can give numerous reports on memory usage on Linux
systems. Unlike existing tools, smem can report proportional set size (PSS),
which is a more meaningful representation of the amount of memory used by
libraries and applications in a virtual memory system.

Because large portions of physical memory are typically shared among
multiple applications, the standard measure of memory usage known as
resident set size (RSS) will significantly overestimate memory usage. PSS
instead measures each application's "fair share" of each shared area to give
a realistic measure.

%prep

%setup -q

%patch0 -p1 -b py3

%build


%install
install -D -p -m 755 smem $RPM_BUILD_ROOT/%{_bindir}/smem
install -D -p -m 644 smem.8 $RPM_BUILD_ROOT/%{_mandir}/man8/smem.8
 

%files
%doc COPYING
%{_bindir}/smem
%{_mandir}/man8/smem.8*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 10 2018 Matthew Miller <mattdm@fedoraproject.org> - 1.5-1
- update to 1.5 tagged release (no new tarballs are forthcoming for this project)
- hard-code python3 as per guidelines

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Dec  9 2013 Matthew Miller <mattdm@mattdm.org> - 1.4-1
- update to 1.4 (small bugfixes)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 28 2013 Matthew Miller <mattdm@mattdm.org> - 1.3-1
- update to 1.3 (small bugfixes)

* Fri Feb 15 2013 Michal Schmidt <mschmidt@redhat.com> - 1.2-4
- Drop the kernel Requires. Using Conflicts would have been acceptable,
  but 2.6.27 is ancient history anyway.
- Remove spec file elements no longer required by current packaging guidelines
  (Group, BuildRoot, explicit buildroot cleaning, defattr).

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 29 2012 Matthew Miller <mattdm@mattdm.org> - 1.2-2
- now we have an upstream tarball. thanks, upstream!

* Mon Oct 29 2012 Matthew Miller <mattdm@mattdm.org> - 1.2-1
- 1.2; no upstream tarball, but tagged in the hg repo.
- resolves bz #757908 (-m and -u fail as non-root)
- resolves bz #864504 (failure in presense of unknown uids)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Aug 10 2011 Matthew Miller <mattdm@mattdm.org> - 1.0-2
- don't hardcode version in source name above, because that
  will lead to me confusing myself. trust me.
- no longer install sample script as documentation

* Wed Aug 10 2011 Matthew Miller <mattdm@mattdm.org> - 1.0-1
- update to 1.0 (bugzilla #678249)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Nov 11 2009 Matthew Miller <mattdm@mattdm.org> - 0.9-1
- update to 0.9
- drop add-hoc index.html doc; add man pages
- drop patches, which are now upstream
- not currently building smemcap.c into an executable -- it's new,
  and would switch the package from being noarch. will deal with that
  in a future update of the package.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu May  7 2009 Matthew Miller <mattdm@mattdm.org> - 0.1-4
- remove smem.pdf at request of upstream
- patch0: 741bd2646ebf -- add GPLv2+ and copyright notice
- patch1: 4320ad746bcc -- check that kernel release >= 2.6.27

* Thu Apr 30 2009 Matthew Miller <mattdm@mattdm.org> - 0.1-3
- fix minor rpmlint concerns raised in review (bz #498490)

* Thu Apr 30 2009 Matthew Miller <mattdm@mattdm.org> - 0.1-2
- whoops -- fixed group

* Thu Apr 30 2009 Matthew Miller <mattdm@mattdm.org> - 0.1-1
- initial specfile
- note gplv2+ license -- added in svn and will be in next code release
