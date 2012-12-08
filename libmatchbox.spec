%define major 	1
%define libname %mklibname mb %major
%define develname %mklibname -d mb

Summary: 	Libraries for the Matchbox Desktop
Name: 		libmatchbox
Version: 	1.9
Release: 	11
URL: 		http://matchbox-project.org
License: 	LGPLv2+
Group: 		System/Libraries
Source0:	http://matchbox-project.org/sources/%{name}/%{version}/%{name}-%{version}.tar.bz2
Patch0:		libmatchbox-1.9-libpng-1.5.patch
Patch1:		libmatchbox-1.9-linkage.patch
BuildRequires:	libx11-devel
BuildRequires:	libxext-devel
BuildRequires:	libxft-devel
BuildRequires:	pkgconfig(pango) pkgconfig(pangoxft)
BuildRequires:	png-devel
BuildRequires:	jpeg-devel
BuildRequires:	Xsettings-client-devel

%description
Matchbox is a base environment for the X Window System running on non-desktop
embedded platforms such as handhelds, set-top boxes, kiosks and anything else
for which screen space, input mechanisms or system resources are limited.

%package -n	%{libname}
Group:		System/Libraries
Summary:	Inter-toolkit configuration settings

%description -n %{libname}
Libraries for the Matchbox Desktop.

%package -n %{develname}
Group:          Development/C
Summary:        Static libraries and header files from %{name}
Provides:	matchbox-devel = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	libmb-devel = %{version}-%{release}
Requires:       %{libname} = %{version}-%{release}
Obsoletes:	%mklibname -d mb 1

%description -n %{develname}
Static libraries and header files from %{name}

%prep
%setup -q
%apply_patches

%build
%configure2_5x --enable-xsettings --enable-png --enable-jpeg --enable-pango
%make CFLAGS="%optflags `pkg-config --cflags pango pangoxft`"

%install
%makeinstall_std
rm -rf %{buildroot}%{_libdir}/*.la

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%{_libdir}/*.a
%{_includedir}/libmb/*.h


%changelog
* Tue Jan 31 2012 Bernhard Rosenkraenzer <bero@bero.eu> 1.9-11
+ Revision: 769968
- Drop dependency on libpng 1.2

  + Oden Eriksson <oeriksson@mandriva.com>
    - attempt to relink against libpng15.so.15

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.9-9
+ Revision: 662380
- mass rebuild

* Sat Feb 05 2011 Funda Wang <fwang@mandriva.org> 1.9-8
+ Revision: 636046
- rebuild
- tighten BR

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 1.9-7mdv2011.0
+ Revision: 602575
- rebuild

* Sun Jan 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.9-6mdv2010.1
+ Revision: 488778
- rebuilt against libjpeg v8

* Sat Aug 15 2009 Oden Eriksson <oeriksson@mandriva.com> 1.9-5mdv2010.0
+ Revision: 416622
- rebuilt against libjpeg v7

* Tue Dec 16 2008 Adam Williamson <awilliamson@mandriva.org> 1.9-4mdv2009.1
+ Revision: 314724
- rebuild
- small style cleanups

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Nov 05 2007 Funda Wang <fwang@mandriva.org> 1.9-3mdv2008.1
+ Revision: 105991
- fix devel package name

* Mon Nov 05 2007 Funda Wang <fwang@mandriva.org> 1.9-2mdv2008.1
+ Revision: 105980
- New devel package policy


* Thu Jan 18 2007 Jérôme Soyer <saispo@mandriva.org> 1.9-1mdv2007.0
+ Revision: 110260
- New release 1.9
- Import libmatchbox

* Tue Mar 21 2006 Austin Acton <austin@mandriva.org> 1.8-1mdk
- New release 1.8

* Fri May 13 2005 Austin Acton <austin@mandriva.org> 1.7-1mdk
- New release 1.7
- fix URLs

* Mon Jan 24 2005 Austin Acton <austin@mandrake.org> 1.6-1mdk
- 1.6

* Tue Jan 04 2005 Austin Acton <austin@mandrake.org> 1.5-1mdk
- 1.5

* Thu Sep 30 2004 Austin Acton <austin@mandrake.org> 1.4-1mdk
- 1.4

* Tue Aug 24 2004 Austin Acton <austin@mandrake.org> 1.3-1mdk
- 1.3

* Wed Jul 21 2004 Austin Acton <austin@mandrake.org> 1.2-1mdk
- initial package

